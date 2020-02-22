import os
import shutil
import json

import numpy as np
from sklearn.cluster import AgglomerativeClustering
import MDAnalysis

from get_confidence_score import get_confidence_score
from get_concavity_score import get_concavity_score
from get_dock_score import get_dock_score
from get_all_ca_pos import get_all_ca_pos
from change_b_factor_from_dict import change_b_factor_from_dict
from cluster_trajectory import cluster_trajectory


def predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name, apo_pdb_loc,
                    clust_max_dist=11, ml_score_thresh=0.8, ml_std_thresh=0.25,
                    dock_extra_space=8):
    """Predict the locations of binding pockets in an MD trajectory.

    This is the function that is expected to be called by users.  It uses a novel algorithm
    to predict where in an MD trajectory there are binding pockets.

    Parameters
    ----------
    psf_loc : string
        The path to the psf file.
    dcd_loc : string
        The path to the dcd loc.
    output_dir : string
        The name of the directory where the output is stored.
        If the directory already exists, its contents will be overwritten.
    num_clusters : int
        The number of clusters of the MD trajectory to create and analyze.
    run_name : string
        The name of this function call.  It should probably be similar to output_dir.
    apo_pdb_loc : string
        The path to the PDB file of the "apo" structure before MD has started.  This is
        compared with the frames from the MD trajectory.
    clust_max_dist : float, optional
        The distance threshold (in Angstroms) to determine if a residue with a high ML
        score should be included in a cluster of other high-scoring residues.  The default
        value is 11.
    ml_score_thresh : float, optional
        The ML confidence score threshold for determining if a residue is "high-scoring".  It
        must be between 0 and 1.  The default value is 0.8
    ml_std_thresh : float, optional
        The algorithm ignores residues that have high ML confidence scores in all frames.  It
        does this by ignoring residues for which the standard deviation of the confidence scores
        among MD snapshots is less than ml_std_thresh.  This number must be between 0 and 1.  The
        default value is 0.25.
    dock_extra_space : float, optional
        The space (in Angstroms) added to each side of the predicted site when
        determining the region to perform docking in.  If this value is too big, then
        AutoDock Vina won't adequately sample all possible poses.  If the value is too small,
        then the fragments will be trapped in the pocket and the dock scores will be inaccurately
        high.  The default value is 8.

    Returns
    -------
    None

    """


    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)

    func_out_file_loc = "%s/%s_output.txt" %(output_dir, run_name)
    with open(func_out_file_loc, "w") as func_out_file:
        func_out_file.truncate()

    universe, cluster_object = cluster_trajectory(psf_loc, dcd_loc, output_dir, num_clusters, 0)

    # Initialization
    ml_scores_list = {}
    ml_scores_list_str = {} # needed for writing file

    # Find the concavity scores and alpha-carbon positions for the apo structure.
    # These are calculated here (instead of in get_confidence_score) so that they only
    # need to be calculated once, instead of being calculated each iteration.
    apo_conc_scores = get_concavity_score(apo_pdb_loc, "apo", "%s/apo_conc" %(output_dir))
    apo_ca_pos_dict = get_all_ca_pos(apo_pdb_loc)

    # Iterate over the centroid of each cluster of MD frames.  In each iteration,
    # call get_confidence_score.
    for centroid_index in cluster_object.get_centroids():
        # Run the ML algorithm on the PDB file of the centroid.
        centroid_conf_dir = "%s/centroid_%d_conf" %(output_dir, centroid_index)
        centroid_pdb_loc = "%s/centroid_%d.pdb" %(output_dir, centroid_index)
        ml_conf_this_cluster = get_confidence_score(centroid_pdb_loc,
                                                    "centroid_%d" %(centroid_index),
                                                    centroid_conf_dir,
                                                    apo_conc_scores,
                                                    apo_ca_pos_dict)
        residues = ml_conf_this_cluster.keys() # Should always be the same for a given protein.
        for residue in residues:
            if residue not in ml_scores_list.keys(): # First iteration
                ml_scores_list[residue] = {centroid_index : ml_conf_this_cluster[residue]}
                ml_scores_list_str[residue] = {str(centroid_index) : ml_conf_this_cluster[residue]}
            else:
                ml_scores_list[residue][centroid_index] = ml_conf_this_cluster[residue]
                ml_scores_list_str[residue][str(centroid_index)] = ml_conf_this_cluster[residue]

    # The goal is to find clusters of high-scoring residues that are near each other;
    # each cluster is a binding site. The clustering is iterative.  A residue should be
    # added to a cluster if the residue is within clust_max_dist of a residue in the cluster.
    # The clusters may change between centroids, so the procedure must be done for each
    # centroid.  The procedure is:
    #     * For each high-scoring residue, create a list of other residues within
    #       clust_max_dist.
    #     * Create a "distance matrix" of the "distances" between high-scoring residues.
    #       But instead of the actual distances, put 1 if the resisidues are within
    #       clust_max_dist, and put 25 (an arbitrary high number) otherwise.  This is
    #       confusing, but easier to code than a real residue-wise distance matrix.  It
    #       should have the same effect as the actual distance matrix would when it is
    #       passed to the clustering algorithm.
    #     * Use scikit-learn's AgglomerativeClustering to get the clusters.
    # The result is a set of clusters of high-scoring residues.  Each cluster is as big
    # as possible without including a residue more than clust_max_dist from another
    # residue in the cluster.

    # Each key in nearby_residues_dict is a centroid index.  Each value is a dictionary of
    # the form {high-scoring_residue : [nearby_residues]}.  Note that not all nearby
    # residues are high-scoring.
    nearby_residues_dict = {}
    for residue, scores_for_this_residue in ml_scores_list.items():
        vals = np.array(list(scores_for_this_residue.values()))
        std = vals.std()
        for centroid, score in scores_for_this_residue.items():
            if (score > ml_score_thresh) and (std > ml_std_thresh):
                # The next line looks unnecessary, but it is needed for MDAnalysis to
                # be working on the correct frame.
                centroid_frame = universe.trajectory[centroid]
                centroid_prot = universe.select_atoms("protein")
                search_centroid = MDAnalysis.lib.NeighborSearch.AtomNeighborSearch(centroid_prot)
                resnum = int(residue[0:-2])
                chain = residue[-1]
                curr_chain_and_resnum_sel = "segid PRO%s and resnum %d" %(chain, resnum)
                curr_chain_and_resnum = universe.select_atoms(curr_chain_and_resnum_sel)
                nearby_residue_group = search_centroid.search(curr_chain_and_resnum,
                                                              clust_max_dist, "R")
                nearby_residue_list = []
                for res in nearby_residue_group:
                    nearby_residue_list.append("%s:%s" %(res.resnum, res.segid[3]))
                # When a centroid is encountered for the first time, add it to the
                # dictionary.
                if centroid not in nearby_residues_dict.keys():
                    nearby_residues_dict[centroid] = {}
                nearby_residues_dict[centroid][residue] = nearby_residue_list
    # nearby_residues_dict stores, for each high-scoring residue in each centroid, which
    # other residues are nearby.  This may include both "high-scoring" residues
    # (highlighted by the ML algorithm) and other residues not selected by ML.  Since
    # the goal is to find clusters of high-scoring residues, the other residues must be
    # separated out.  high_scoring_neighbors is like nearby_residues_dict, with the
    # following differences:
    #     * It is re-initialized for each centroid.  Thus at any given moment, it
    #       only contains data about 1 centroid.
    #     * It lists only the high-scoring neighbors.
    # After high_scoring_neighbors is constructed, use it to create the distance
    # matrix.  Then use the distance matrix to cluster the residues.

    # The next 2 lines are initializations.
    pymol_load_snaps = "" # PyMOL code to load each snapshot.
    pymol_show_resis = "" # PyMOL code to show residues selected by ML.
    all_cmd_str = "" # PyMOL code for boxes.
    for centroid in nearby_residues_dict.keys():
        print("centroid:", centroid)
        dock_scores_all_clusters = {} # Initialization for PyMOL visualization.
        centroid_frame = universe.trajectory[centroid]
        # Each key is a residue.  Each value is a list of high-scoring neighbors.
        high_scoring_neighbors = {}
        for residue in nearby_residues_dict[centroid].keys():
            to_be_added = []
            for other_residue in nearby_residues_dict[centroid].keys():
                if residue in nearby_residues_dict[centroid][other_residue]:
                    to_be_added.append(other_residue)
            high_scoring_neighbors[residue] = to_be_added
        dist_mat = []
        order = []
        for residue in nearby_residues_dict[centroid].keys():
            to_be_added = []
            for other_residue in nearby_residues_dict[centroid].keys():
                # Set the distance to an arbitrary low number if the residues are close,
                # to each other, or an arbitrary high number if they are far apart.
                if other_residue in high_scoring_neighbors[residue]:
                    to_be_added.append(1)
                else:
                    to_be_added.append(20)
            dist_mat.append(to_be_added)
            order.append(residue)
        dist_mat_array = np.asarray(dist_mat, dtype=np.int8)
        # If there is more than 1 high-scoring residue,  then use scikit's Agglomerative Clustering.
        # But it crashes if given only 1 point.
        if len(dist_mat_array) > 1:
            clustering_object = AgglomerativeClustering(linkage="single", distance_threshold=10,
                                                        compute_full_tree=True,
                                                        affinity="precomputed", n_clusters=None)
            clustering_fit = clustering_object.fit(dist_mat_array)
            for cluster in range(clustering_fit.n_clusters_):
                residues_in_cluster = []
                for residue_index in range(len(order)):
                    if clustering_fit.labels_[residue_index] == cluster:
                        residues_in_cluster.append(order[residue_index])
                output_sele_string = "sele cluster_%s, " %(cluster)
                mda_sele_string = ""
                for residue in residues_in_cluster:
                    resnum = int(residue[0:-2])
                    chain = residue[-1]
                    output_sele_string += "(chain %s and resi %d) or " %(chain, resnum)
                    mda_sele_string += "(resid %d and segid PRO%s) or " %(resnum, chain)
                output_sele_string = output_sele_string[:-4] # delete the " or " at the end.
                mda_sele_string = mda_sele_string[:-4]
                print("cluster:", cluster, "selection:\n", output_sele_string,
                      "\nResidues:", residues_in_cluster, "\n")
                if len(residues_in_cluster) > 1:
                    high_scoring_selection = universe.select_atoms(mda_sele_string)
                    positions = high_scoring_selection.positions
                    max_x = max(positions[:, 0])
                    min_x = min(positions[:, 0])
                    max_y = max(positions[:, 1])
                    min_y = min(positions[:, 1])
                    max_z = max(positions[:, 2])
                    min_z = min(positions[:, 2])
                    center = [(max_x + min_x)/2, (max_y + min_y)/2, (max_z + min_z)/2]
                    extra_space = 15
                    size = [(max_x - min_x + extra_space),
                            (max_y - min_y + extra_space),
                            (max_z - min_z + extra_space)]
                    fbl = [center[0]-(size[0]/2), center[1]-(size[1]/2), center[2]+(size[2]/2)]
                    fbr = [center[0]+(size[0]/2), center[1]-(size[1]/2), center[2]+(size[2]/2)]
                    ftl = [center[0]-(size[0]/2), center[1]+(size[1]/2), center[2]+(size[2]/2)]
                    ftr = [center[0]+(size[0]/2), center[1]+(size[1]/2), center[2]+(size[2]/2)]
                    bbl = [center[0]-(size[0]/2), center[1]-(size[1]/2), center[2]-(size[2]/2)]
                    bbr = [center[0]+(size[0]/2), center[1]-(size[1]/2), center[2]-(size[2]/2)]
                    btl = [center[0]-(size[0]/2), center[1]+(size[1]/2), center[2]-(size[2]/2)]
                    btr = [center[0]+(size[0]/2), center[1]+(size[1]/2), center[2]-(size[2]/2)]
                    this_cmd_str = ""
                    this_cmd_str += 'cmd.load_cgo([BEGIN, LINES, '
                    for pair in [[fbl, fbr], [fbl, ftl], [fbr, ftr], [ftl, ftr],
                                 [bbl, bbr], [bbl, btl], [bbr, btr], [btl, btr],
                                 [fbl, bbl], [ftl, btl], [fbr, bbr], [ftr, btr]]:
                        this_cmd_str += "VERTEX, %f, %f, %f, VERTEX, %f, %f, %f, " %(pair[0][0], pair[0][1], pair[0][2], pair[1][0], pair[1][1], pair[1][2])
                    this_cmd_str += 'END], "%s_cluster_%s")\n' %(centroid, cluster)
                    all_cmd_str += this_cmd_str
                    prot_name = "centroid_%d_cluster_%d" %(centroid, cluster)
                    centroid_pdb_loc = "%s/centroid_%d.pdb" %(output_dir, centroid)
                    output_dir_dock = "%s/centroid_%d_cluster_%d_dock" %(output_dir,
                                                                         centroid,
                                                                         cluster)
                    dock_scores = get_dock_score(prot_name, centroid_pdb_loc,
                                                 output_dir_dock, True, center, size,
                                                 dock_extra_space)


                    # Use the dock scores to assess the druggability of the predicted
                    # pocket.  This uses the following criteria:
                    #    * Do fragment ligands bind to the residues selected by the ML
                    #      algorithm?  If ligands don't bind, then the site isn't
                    #      druggable.
                    #    * Are ligands more likely to bind to the selected residues than
                    #      to other residues?  If not, then the predicted binding may
                    #      be the result of algorithm errors and/or nonspecific binding.
                    tot_score_pocket = 0
                    tot_score_all = 0
                    for residue in residues_in_cluster:
                        if residue in dock_scores.keys():
                            tot_score_pocket += dock_scores[residue]
                    for residue, score in dock_scores.items():
                        tot_score_all += score
                        if residue in dock_scores_all_clusters:
                            dock_scores_all_clusters[residue] += score
                        else:
                            dock_scores_all_clusters[residue] = score
                    mean_score_pocket = tot_score_pocket / len(residues_in_cluster)
                    mean_score_all = tot_score_all / len(dock_scores.values())
                    with open(func_out_file_loc, "a") as func_out_file:
                        func_out_file.write("centroid: %d     cluster: %d\n\n" %(centroid, cluster))
                        func_out_file.write("selection string:\n%s\n\n" %(output_sele_string))
                        # Print the dock scores, sorted from highest to lowest.  Start
                        # by creating a list of tuples (score, residue) sorted by score.
                        # Then create another list of tuples (residue, score).
                        scores_sort_rev = sorted(((score, res) for res, score in
                                                  dock_scores.items()), reverse=True)
                        scores_str = ""
                        for item in scores_sort_rev:
                            scores_str += "%s %s\t" %(item[1], item[0])
                        #scores_sort = [(entry[1], entry[0]) for entry in scores_sort_rev]
                        func_out_file.write(scores_str)
                        print(scores_str)
                        dict_for_out = {"dock_scores" : dock_scores}
                        func_out_file.write(json.dumps(dict_for_out))
                        func_out_file.write("\n")
                        for residue in residues_in_cluster:
                            func_out_file.write("%s " %(residue))
                        func_out_file.write("\n")
                        print("residues_in_cluster", residues_in_cluster)
                        func_out_file.write("mean_score_pocket = %f     "
                                            "mean_score_all = %f\n\n\n\n\n" %(mean_score_pocket,
                                                                              mean_score_all))
                else:
                    with open(func_out_file_loc, "a") as func_out_file:
                        func_out_file.write("centroid: %d     cluster: %d\n\n" %(centroid, cluster))
                        func_out_file.write("selection string:\n%s\n" %(output_sele_string))
                        func_out_file.write("This cluster has only 1 residue.  It "
                                            "may not be a real binding site.\n\n\n\n\n")
                        print("This cluster has only 1 residue.  It "
                              "may not be a real binding site.\n\n\n\n\n")
            b_factor_pdb_loc = "%s/%s_b_factor.pdb" %(output_dir, centroid)
            change_b_factor_from_dict("%s/centroid_%d.pdb" %(output_dir, centroid),
                                      dock_scores_all_clusters, b_factor_pdb_loc)
            for residue_and_chain in high_scoring_neighbors.keys():
                resi = residue_and_chain[:-2]
                chain = residue_and_chain[-1]
                pymol_show_resis += ("show sticks, %s_b_factor and chain %s and "
                                     "resi %s\n" %(centroid, chain, resi))
            pymol_load_snaps += "load %s_b_factor.pdb\n" %(centroid)
        else:
            residue = order[0]
            resnum = int(residue[0:-2])
            chain = residue[-1]
            output_sele_string = " sele only_res, (chain %s and resi %d)" %(chain, resnum)
            print(("This centroid (number %s) doesn't have multiple high-scoring "
                   "residues.  It isn't predicted to have any cryptic pockets.  The"
                   "selection string is:\n" %(centroid)),
                  output_sele_string, "\nResidues:", residue, "\n")
            with open(func_out_file_loc, "a") as func_out_file:
                func_out_file.write("This centroid (number %s) doesn't have multiple "
                                    "high-scoring residues.  It isn't predicted to "
                                    "have any cryptic pockets.\n" %(centroid))
            mda_sele_string = "(resid %d and segid PRO%s)" %(resnum, chain)
            residues_in_cluster = [residue]
    # Write 2 pymol scripts.  One has a white background; the ML predictions are
    # displayed in black.  The other has a black background; the ML predictions are
    # displayed in white.
    pymol_script_bg_white_loc = "%s/display_white_bg.pml" %(output_dir)
    with open(pymol_script_bg_white_loc, "w") as pymol_script_bg_white_file:
        pymol_script_bg_white_file.write("from pymol.cgo import *\n")
        pymol_script_bg_white_file.write(pymol_load_snaps)
        pymol_script_bg_white_file.write("spectrum b\n"
                                          "as cartoon\n"
                                          "cartoon putty\n")
        pymol_script_bg_white_file.write(pymol_show_resis)
        pymol_script_bg_white_file.write(all_cmd_str)
        pymol_script_bg_white_file.write("set stick_color, black\n")
        pymol_script_bg_white_file.write("set bg_rgb,[1,1,1]")

    pymol_script_bg_black_loc = "%s/display_black_bg.pml" %(output_dir)
    with open(pymol_script_bg_black_loc, "w") as pymol_script_bg_black_file:
        pymol_script_bg_black_file.write("from pymol.cgo import *\n")
        pymol_script_bg_black_file.write(pymol_load_snaps)
        pymol_script_bg_black_file.write("spectrum b\n"
                                          "as cartoon\n"
                                          "cartoon putty\n")
        pymol_script_bg_black_file.write(pymol_show_resis)
        pymol_script_bg_black_file.write(all_cmd_str)
        pymol_script_bg_black_file.write("set stick_color, white\n")
