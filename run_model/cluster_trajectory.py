import os
import subprocess

import MDAnalysis
from MDAnalysis.analysis.encore import clustering
from get_list_of_segids import get_list_of_segids


def cluster_trajectory(psf_loc, dcd_loc, output_dir, num_clusters, seed=None):
    """Cluster an MD trajectory, and create a PDB file for each cluster.

    The script uses MDAnalysis to cluster the trajectory.  It writes a PDB
    file of each cluster's centroid, called centroid_[number]_no_chain.pdb.
    However, this PDB file separates chains
    by the Segid column instead of the Chain column.  The function then writes
    another PDB file in which chains are noted in the Chain column.  This file
    is called centroid_[number].pdb

    Parameters
    ----------
    psf_loc : string
        The path to the psf file.
    dcd_loc : string
        The path to the dcd loc.
    output_dir : string
        The name of the directory where the output is stored.  This directory
        should already exist.  Any existing contents will NOT be deleted, but
        they may be overwritten.
    num_clusters : int
        The number of clusters to create
    seed : int
        The seed to use for MDAnalysis's clustering.

    Returns
    -------
    universe : MDAnalysis universe object
        The universe object containing the trajectory.
    cluster_object : MDAnalysis cluster object
        The cluster object created by MDAnalysis.

    """

    # Use KMeans to cluster the trajectory.  The clustering is used to choose which
    # frames of the trajectory are analyzed.
    universe = MDAnalysis.Universe(psf_loc, dcd_loc)
    kmeans = clustering.ClusteringMethod.KMeans(num_clusters)
    if seed is None:
        cluster_object = clustering.cluster.cluster(universe, method=kmeans)
    else:
        cluster_object = clustering.cluster.cluster(universe, method=kmeans,
                                                    random_state=seed)

    # Iterate over the centroid of each cluster of MD frames.  In each iteration,
    # do the following:
    #     * Write the centroid as a PDB file.
    #     * Reformat the PDB file so that it uses chains instead of segids.
    #     * Call get_confidence_score.
    for centroid_index in cluster_object.get_centroids():
        # The next like is necessary so that MDAnalysis is working on the correct frame.
        centroid_frame = universe.trajectory[centroid_index]
        centroid_prot = universe.select_atoms("protein")
        centroid_pdb_loc = "%s/centroid_%d.pdb" %(output_dir, centroid_index)
        centroid_prot.write(centroid_pdb_loc)
        # ConCavity (which the ML code uses) ignores segids.  So I need a version of the
        # PDB file where the segid letter is put in the chain column.
        list_of_segids = get_list_of_segids(centroid_pdb_loc)
        list_of_chains = []
        for segid in list_of_segids:
            list_of_chains.append(segid[-1])
        # The naming of ConCavity's output files depends on the name of the input PDB.
        # So the PDB input (with chains) should be named prot_name.pdb.  But I want to
        # keep a copy of the original PDB for reference.
        centroid_pdb_loc_renamed = "%s/centroid_%d_no_chain.pdb" %(output_dir,
                                                                   centroid_index)
        os.rename(centroid_pdb_loc, centroid_pdb_loc_renamed)
        # Create and run a PyMOL script that reformats the PDB file.  The script should
        # be in output_dir.  But the function shouldn't permanently change the working
        # directory.  So it does the following:
        #     * Store the location of the original working directory.
        #     * Move to output_dir.
        #     * Create and run the PyMOL script.
        #     * Change back to the original directory.
        original_working_dir = os.getcwd()
        os.chdir(output_dir)
        # renamed_pdb_in_dir_loc is like centroid_pdb_loc_renamed, except that the
        # former path doesn't include output_dir.  The same is true of
        # centroid_pdb_in_dir_loc and centroid_pdb_loc
        renamed_pdb_in_dir_loc = "centroid_%d_no_chain.pdb" %(centroid_index)
        centroid_pdb_in_dir_loc = "centroid_%d.pdb" %(centroid_index)
        # Iteratively create a PyMOL script to rename the chains according to the segids.
        segid_to_chain_script = "load %s\n" %(renamed_pdb_in_dir_loc)
        for i in range(len(list_of_segids)):
            cmd_text = ("alter (segid %s), chain=\"%s\"\n" %(list_of_segids[i],
                                                             list_of_chains[i]))
            segid_to_chain_script += cmd_text
        segid_to_chain_script += "sort\n" # Necessary according to the PyMOL documentation.
        segid_to_chain_script += "save %s" %(centroid_pdb_in_dir_loc)
        segid_to_chain_script_loc = "centroid_%d_segid_to_chain.pml" %(centroid_index)
        with open(segid_to_chain_script_loc, "w") as segid_to_chain_script_file:
            segid_to_chain_script_file.write(segid_to_chain_script)
        subprocess.run("pymol -cq %s" %(segid_to_chain_script_loc), shell=True)
        os.chdir(original_working_dir)
    return universe, cluster_object
