import errno
import os
import subprocess
import shutil
import re
import math

from get_list_of_segids import get_list_of_segids

### WARNING: The values of mgltools_loc, pythonsh_loc, and prepare_receptor4_loc
# must be set to the correct values before running TACTICS.
mgltools_loc = "~/MGLTools-1.5.6/"
pythonsh_loc = "%s/bin/pythonsh" %(mgltools_loc)
prepare_receptor4_loc = "%s/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py" %(mgltools_loc)


def get_dock_score(prot_name, pdb_file_loc, output_dir, segid, center=None, size=None,
                   extra_space=8):
    """Get each residue's dock using the ConCavity algorithm.

    The script creates output_dir, or overwrites it if it already exists.
    It runs AutoDock Vina on the protein, using 16 fragment ligands.  The dock score is the
    total number of poses in which the ligand is within 3.5 Angstroms of the residue.

    Parameters
    ----------
    prot_name : string
        The name of the protein, to be included in the names of output files.
        E.g. the PDB ID.
    pdb_file_loc : string
        The path to the pdb file that Vina is run on.  The protein's chains
        may be specified in either the Chain or Segid column.
    output_dir : string
        The name of the directory where the output should be stored.
        If the directory already exists, its contents will be overwritten.
    segid : bool
        Whether the chain info is stored in the Segid column (instead of in
        the Chain column).  If True, then the function will create a reformatted
        PDB file with the chain listed in the Chain column.
    center : list of floats of format [x_coord, y_coord, z_coord], optional
        If specified, then the docking will be confined to an area centered around
        center.  If center is given, then size should also be given.
    size : list of floats of format [x_size, y_size, z_size], optional
        If specified, then the docking will be confined to an area of this size.
        If size is given, then center should also be given.
    extra_space : float, optional
        The space (in Angstroms) added to each side of the predicted site when
        determining the region to perform docking in.  If this value is too big, then
        AutoDock Vina won't adequately sample all possible poses.  If the value is too small,
        then the fragments will be trapped in the pocket and the dock scores will be inaccurately
        high.  The default value is 8.

    Returns
    -------
    results_for_all_ligands : dictionary
        Stores the score for each residue.  Keys are strings of the form resnum:chain.

    """


    print("running get_dock_score(%s, %s, %s)" %(prot_name, pdb_file_loc, output_dir))
    if not os.path.isfile(pdb_file_loc):
        # errno.ENOENT is the error number for nonexistent files.
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), pdb_file_loc)
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)


    if segid:
        # Create a version of the PDB file in which the chains are
        # labelled according to the segids.  Change pdb_file_loc to the
        # new file, so that the code is run on it.
        list_of_segids = get_list_of_segids(pdb_file_loc)
        list_of_chains = []
        # The variable prot_segid (defined below) is different from the function
        # argument segid.
        for prot_segid in list_of_segids:
            list_of_chains.append(prot_segid[-1])
        shutil.copyfile(pdb_file_loc, "%s/%s_no_chain.pdb" %(output_dir, prot_name))
        original_working_dir = os.getcwd()
        os.chdir(output_dir)

        # Iteratively create a PyMOL script to rename the chains according to the segids.
        segid_to_chain_script = "load %s_no_chain.pdb\n" %(prot_name)
        for i in range(len(list_of_segids)):
            segid_to_chain_script += "alter (segid %s), chain=\"%s\"\n" %(list_of_segids[i],
                                                                          list_of_chains[i])
        segid_to_chain_script += "sort\n" # Necessary according to the PyMOL documentation.
        segid_to_chain_script += "save %s.pdb" %(prot_name)
        segid_to_chain_script_loc = "%s_segid_to_chain.pml" %(prot_name)
        with open(segid_to_chain_script_loc, "w") as segid_to_chain_script_file:
            segid_to_chain_script_file.write(segid_to_chain_script)
        subprocess.run("pymol -cq %s" %(segid_to_chain_script_loc), shell=True)
        os.chdir(original_working_dir)
        pdb_file_loc = "%s/%s.pdb" %(output_dir, prot_name)


    prot_pdbqt_loc = "%s/%s.pdbqt" %(output_dir, prot_name)
    subprocess.run(("%s %s -r %s -U nphs_lps_waters -o %s" %(pythonsh_loc, prepare_receptor4_loc, pdb_file_loc, prot_pdbqt_loc)),
                   shell=True)
    print("done with prepare_receptor4")

    if (center is None) or (size is None):
        print("finding the center and size of the pdb file.")
        with open("%s/vmd_script.tcl" %(output_dir), "w") as vmd_script:
            center_coords_loc = "%s/%s_center_coords.txt" %(output_dir, prot_name)
            minmax_coords_loc = "%s/%s_minmax_coords.txt" %(output_dir, prot_name)
            vmd_script.write("mol new %s\n" %(pdb_file_loc))
            vmd_script.write("set file [open \"%s\" w]\n" %(center_coords_loc))
            vmd_script.write("set everyone [atomselect top all]\n")
            vmd_script.write("puts $file [ measure center $everyone]\n")
            vmd_script.write("close $file\n")
            vmd_script.write("set file [open \"%s\" w]\n" %(minmax_coords_loc))
            vmd_script.write("puts $file [ measure minmax $everyone]\n")
            vmd_script.write("close $file\n")
            vmd_script.write("mol delete 0\n")
            vmd_script.write("quit")
        subprocess.run("vmd -dispdev text -e %s/vmd_script.tcl" %(output_dir), shell=True)
        with open(center_coords_loc, "r") as center_coords_opened:
            center_coords_strings = center_coords_opened.readline().split()
            center_coords = [float(coord) for coord in center_coords_strings]
        with open(minmax_coords_loc, "r") as minmax_coords_opened:
            min_max_coords_line = minmax_coords_opened.readline()
            re_string_for_minmax = (r"\{([\-0-9.]+) ([\-0-9.]+) ([\-0-9.]+)\} \{([\-0-9.]+) "
                                    r"([\-0-9.]+) ([\-0-9.]+)\}")
            re_match_for_minmax = re.match(re_string_for_minmax, min_max_coords_line)
            all_minmax_coords = re_match_for_minmax.groups()
            min_coords = [float(coord) for coord in all_minmax_coords[0:3]]
            max_coords = [float(coord) for coord in all_minmax_coords[3:6]]

    print("running autodock")
    autodock_script_loc = "%s/run_autodock.sh" %(output_dir)
    with open(autodock_script_loc, "w") as autodock_script:
        autodock_script.write("#!/bin/bash\n")
        ligand_names = ["ethane", "EOH", "IPA", "TBU", "CCN", "NME", "DMF", "2F2", "HBX", "BNZ",
                        "CHX", "IPH", "ACM", "ACN", "ACE", "URE"]
        #ligand_names = ["ethane", "EOH"]
        for ligand_name in ligand_names:
            # The ligand pdbqt file needs to be in the correct directory.
            original_ligand_pdbqt_loc = "ligands/%s_ideal.pdbqt" %(ligand_name)
            ligand_pdbqt_loc = "%s/%s_ideal.pdbqt" %(output_dir, ligand_name)
            shutil.copyfile(original_ligand_pdbqt_loc, ligand_pdbqt_loc)
            if size is None:
                size_x = max_coords[0] - min_coords[0] + extra_space
                size_y = max_coords[1] - min_coords[1] + extra_space
                size_z = max_coords[2] - min_coords[2] + extra_space
            else:
                size_x = size[0]
                size_y = size[1]
                size_z = size[2]
            if center is not None:
                center_coords = center
            autodock_script.write("vina --receptor %s --ligand %s --center_x %f --center_y %f "
                                  "--center_z %f --size_x %f --size_y %f --size_z %f\n"
                                  %(prot_pdbqt_loc, ligand_pdbqt_loc, center_coords[0],
                                    center_coords[1], center_coords[2], size_x, size_y, size_z))
            output_pdbqt_default = "%s/%s_ideal_out.pdbqt" %(output_dir, ligand_name)
            output_pdbqt_renamed = "%s/%s_%s.pdbqt" %(output_dir, ligand_name, prot_name)
            output_pdb = "%s/%s_%s.pdb" %(output_dir, ligand_name, prot_name)
            autodock_script.write("mv %s %s\n" %(output_pdbqt_default, output_pdbqt_renamed))
            autodock_script.write("obabel %s -O %s -xr\n" %(output_pdbqt_renamed, output_pdb))

    subprocess.call("chmod +x %s" %(autodock_script_loc), shell=True)
    subprocess.call(autodock_script_loc, shell=True)

    print("analyzing results")

    def calc_dist(point_1, point_2):
        # point_1 and point_2 should be lists of numbers, of the form [x, y, z].
        return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2 +
                         (point_1[2] - point_2[2]) ** 2)


    results_for_all_ligands = {}
    for ligand_name in ligand_names:
        output_pdb = "%s/%s_%s.pdb" %(output_dir, ligand_name, prot_name)
        with open(output_pdb, "r") as output_pdb_opened:
            output_pdb_lines = output_pdb_opened.readlines()
        with open(pdb_file_loc, "r") as protein_file_opened:
            protein_file_lines = protein_file_opened.readlines()

        # Each key of residues_near_each_pose is a ligand_pose_num value; each dict val is a list
        # of residues close to that pose.
        residues_near_each_pose = {}
        for ligand_line in output_pdb_lines:
            if (len(ligand_line) >= 6) and (re.match(r"MODEL\s*\d", ligand_line)):
                ligand_pose_num = int(re.match(r"MODEL\s*(\d)", ligand_line).groups()[0])
                residues_near_each_pose[ligand_pose_num] = []
            if (len(ligand_line) >= 21) and (ligand_line[0:4] == "ATOM"):
                for protein_line in protein_file_lines:
                    if (len(protein_line) >= 21) and (protein_line[0:4] == "ATOM"):
                        protein_pos = [float(protein_line[30:38]), float(protein_line[38:46]),
                                       float(protein_line[46:54])]
                        ligand_pos = [float(ligand_line[30:38]), float(ligand_line[38:46]),
                                      float(ligand_line[46:54])]
                        dist = calc_dist(protein_pos, ligand_pos)
                        prot_resnum_modeller = protein_line[22:27].strip()
                        prot_chain_modeller = protein_line[21]
                        prot_resnum_with_chain_mod = "%s:%s" %(prot_resnum_modeller,
                                                               prot_chain_modeller)
                        if (dist < 3.5) and (prot_resnum_with_chain_mod not in
                                             residues_near_each_pose[ligand_pose_num]):
                            residues_near_each_pose[ligand_pose_num].append(prot_resnum_with_chain_mod)

        # Each key of score_for_this_ligand is a residue index; each dict val is the number of
        # poses in which that residue is close to the ligand.
        score_for_this_ligand = {}
        for residue_list in residues_near_each_pose.values():
            for residue in residue_list:
                if residue in score_for_this_ligand:
                    score_for_this_ligand[residue] += 1
                else:
                    score_for_this_ligand[residue] = 1

        for residue in score_for_this_ligand.keys():
            if residue in results_for_all_ligands:
                results_for_all_ligands[residue] += score_for_this_ligand[residue]
            else:
                results_for_all_ligands[residue] = score_for_this_ligand[residue]
    return results_for_all_ligands
