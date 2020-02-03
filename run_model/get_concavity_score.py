"""This contains the function
get_concavity_score(pdb_file_loc, prot_name, output_dir, segid).

"""
import os
import shutil
import subprocess


def get_concavity_score(pdb_file_loc, prot_name, output_dir):
    """Get each residue's score using the ConCavity algorithm.

    The script creates output_dir, or overwrites it if it already exists.
    It runs ConCavity then parses the output.  Note that pdb_file_loc should
    have chains listed in the Chain column, NOT the Segid column.

    Parameters
    ----------
    pdb_file_loc : string
        The path to the pdb file that ConCavity is run on.  The file
        should use the Chain column if multiple chains are present.
    prot_name : string
        The name of the protein, to be included in the names of output files.
        E.g. the PDB ID.
    output_dir : string
        The name of the directory where the ConCavity output should be stored.
        If the directory already exists, its contents will be overwritten.

    Returns
    -------
    dict_res_to_score : dictionary
        Stores the score for each residue.  Keys are strings of the form resnum:chain.

    """


    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)
    shutil.copyfile(pdb_file_loc, "%s/%s.pdb" %(output_dir, prot_name))
    # Concavity puts its output in the current working directory.  So the code must
    # cd into that directory.  It should cd back to the original directory before exiting.
    original_working_dir = os.getcwd()
    os.chdir(output_dir)

    subprocess.run("concavity %s.pdb conc_out" %(prot_name), shell=True)
    dict_res_to_score = {}

    conc_out_pdb_loc = "%s_conc_out_residue.pdb" %(prot_name)
    with open(conc_out_pdb_loc, "r") as conc_out_pdb:
        conc_out_pdb_lines = conc_out_pdb.readlines()
    for line in conc_out_pdb_lines:
        if (len(line) >= 66) and (line[0:4] == "ATOM"):
            score = float(line[60:66].strip())
            resnum = line[22:27].strip()
            chain = line[21]
            resnum_and_chain = "%s:%s" %(resnum, chain)
            dict_res_to_score[resnum_and_chain] = score

    os.chdir(original_working_dir)
    return dict_res_to_score
