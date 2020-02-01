import os
import shutil
import subprocess


def get_concavity_score(pdb_file_loc, prot_name, output_dir):
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
            if resnum_and_chain not in dict_res_to_score:
                dict_res_to_score[resnum_and_chain] = score
    os.chdir(original_working_dir)
    return dict_res_to_score 
