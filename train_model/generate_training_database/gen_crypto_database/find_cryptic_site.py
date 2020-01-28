"""This script should be used in step 9 of the procedure for regenerating the
Cryptosite database.  It reads pdbs_and_ligands.csv.  It generates
cryptic_site_locations.csv.  IMPORTANT: cryptic_site_locations.csv must be
edited after creation; see the documentation."""

import math

import pandas as pd


def calc_dist(point_1, point_2):
    # point_1 and point_2 should be lists of numbers, of the form [x, y, z].
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2 + (point_1[2] - point_2[2]) ** 2)


def find_cryptic_site(holo_pdb_file, ligand_id, chain_id):
    # Returns a dictionary whose keys are the residue numbers of ligands and whose values are the residue numbers of amino acids with at
    # least 1 atom within 5 angstroms of at least one atom of the ligand.

    # Step 1: Get the lines of the PDB file for the chain of interest.
    protein_lines_to_keep = []
    with open(holo_pdb_file, "r") as holo_pdb_file_opened:
        for line in holo_pdb_file_opened.readlines():
            if (len(line) >= 21) and (line[0:4] == "ATOM") and (line[21] == chain_id):
               protein_lines_to_keep.append(line)
    # Step 2: Get the lines of the PDB file for the ligand.
    ligand_lines_to_keep = []
    with open(holo_pdb_file, "r") as holo_pdb_file_opened:
        for line in holo_pdb_file_opened.readlines():
            if (len(line) >= 21) and (line[0:6] == "HETATM") and (line[17:20] == ligand_id):
               ligand_lines_to_keep.append(line)

    # Step 3: Calculate the distances.
    # There may be multiple copies of the ligand.  But only 1 is in the cryptic site.  I don't know which site is cryptic,
    # but I can guess by counting how many amino acid residues are in the site and comparing this with what the supplemental
    # material of the cryptosite paper says.

    # cryptic_site_residues is a dictionary whose keys are ligand molecules and whose values are lists of amino acids within 5 angstroms
    # of the ligand.  Specifically, the key is a tuple (ligand_residue_num, ligand_chain).  This is necessary because some PDB files have
    # different ligands with the same residue number but different chain IDs.
    cryptic_site_residues = {}
    for ligand_line in ligand_lines_to_keep:
        ligand_res_num = ligand_line[22:26]
        ligand_chain = ligand_line[21]
        if (ligand_res_num, ligand_chain) not in cryptic_site_residues:
            cryptic_site_residues[(ligand_res_num, ligand_chain)] = []
    for protein_line in protein_lines_to_keep:
        for ligand_line in ligand_lines_to_keep:
            prot_pos = [float(protein_line[30:38]), float(protein_line[38:46]), float(protein_line[46:54])]
            ligand_pos = [float(ligand_line[30:38]), float(ligand_line[38:46]), float(ligand_line[46:54])]
            if calc_dist(prot_pos, ligand_pos) < 5:
                prot_res_num = protein_line[22:27].strip()
                ligand_res_num = ligand_line[22:26]
                ligand_chain = ligand_line[21]
                # It seems that the authors of the cryptosite paper excluded residues with insertion codes.  (They don't
                # mention this in the paper, but this was the only way I could get the correct number of residues in the sites.)
                if (prot_res_num not in cryptic_site_residues[(ligand_res_num, ligand_chain)]) and (protein_line[26] == " "):
                    cryptic_site_residues[(ligand_res_num, ligand_chain)].append(prot_res_num)
    return cryptic_site_residues





with open("cryptic_site_locations.csv", "w") as site_locations_file:
    site_locations_file.write("apo_pdb_id,apo_chain,holo_pdb_id,holo_chain,ligand_id,ligand_resnum,ligand_chain,site_residues,site_size\n") # Header line.
    df_apo_chain_holo_chain_ligand = pd.read_csv("pdbs_and_ligands.csv")
    for index, row in df_apo_chain_holo_chain_ligand.iterrows():
        pdb_file = "holo_structures/%s.pdb" %(row["holo_pdb_id"].lower())
        cryptic_sites = find_cryptic_site(pdb_file, row["ligand_id"], row["holo_chain"])
        for ligand_resnum_and_chain, list_of_prot_resnums in cryptic_sites.items():
            string_of_prot_resnums = ""
            for prot_resnum in list_of_prot_resnums:
                string_of_prot_resnums += prot_resnum
                string_of_prot_resnums += " " 
            if len(list_of_prot_resnums) >= 5: # All of the real sites have at least 5 residues.  Therefore smaller sites aren't part of the database.
                site_locations_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%d\n" %(row["apo_pdb_id"], row["apo_chain"],
                                                                          row["holo_pdb_id"], row["holo_chain"], 
                                                                          row["ligand_id"], ligand_resnum_and_chain[0], ligand_resnum_and_chain[1],
                                                                          string_of_prot_resnums, len(list_of_prot_resnums)))


