"""This script should be used in step 13 of the procedure for regenerating the
Cryptosite database.  It cryptic_site_locations.csv, residue_codes.json, the
apo pdb files, and the json files in apo_holo_numbering_dicts.  It creates
cryptosite_database.csv, which contains a line for each residue in the
appropriate chain of each apo structure.  It generates
cryptic_site_locations.csv."""

import pandas as pd
import json


df_cryptic_site_residues = pd.read_csv("cryptic_site_locations.csv")

def get_apo_residues_from_pdb(pdb_file, chain_id):
    residue_numbers = []
    residues = []
    with open("residue_codes.json", "r") as residue_codes_json: # Convert 3-letter to 1-letter
        residue_codes = json.load(residue_codes_json)
    with open(pdb_file, "r") as pdb_opened:
        pdb_lines = pdb_opened.readlines()
    for line in pdb_lines:
        if (len(line) >= 21) and (line[0:4] == "ATOM") and (line[21] == chain_id):
            residue_num = line[22:27].strip() # Includes insertion code.
            if residue_num not in residue_numbers:
                residue_numbers.append(residue_num)
                residue = residue_codes[line[17:20]]
                residues.append([residue, residue_num])
    return residues


df_res = pd.DataFrame(columns=["apo_pdb_id", "apo_chain", "apo_resnum",
                                    "holo_pdb_id", "holo_chain", "holo_resnum",
                                    "ligand_id", "ligand_resnum", "ligand_chain",
                                    "residue", "is_cryptic"])
def get_residues(row_of_df_res):
    apo_pdb_file =  "apo_structures/%s.pdb" %(row_of_df_res["apo_pdb_id"].lower())
    chain_id = row_of_df_res["apo_chain"]
    residues = get_apo_residues_from_pdb(apo_pdb_file, chain_id)
    list_of_vals = []
    apo_holo_dict_path = "apo_holo_numbering_dicts/%s_%s.json" %(row_of_df_res["apo_pdb_id"], row_of_df_res["holo_pdb_id"])
    with open(apo_holo_dict_path, "r") as apo_holo_json:
        apo_holo_dict = json.load(apo_holo_json)
    for residue in residues:
        residue_name = residue[0]
        apo_residue_num = residue[1]
        holo_residue_num = apo_holo_dict[apo_residue_num]
        is_cryptic = (holo_residue_num in row_of_df_res["site_residues"].split())
        list_of_vals.append([row_of_df_res["apo_pdb_id"], row_of_df_res["apo_chain"],
                             apo_residue_num, row_of_df_res["holo_pdb_id"],
                             row_of_df_res["holo_chain"], holo_residue_num,
                             row_of_df_res["ligand_id"], row_of_df_res["ligand_resnum"].strip(),
                             row_of_df_res["ligand_chain"], residue_name, is_cryptic])
    return pd.DataFrame(list_of_vals, columns=["apo_pdb_id", "apo_chain", "apo_resnum",
                                    "holo_pdb_id", "holo_chain", "holo_resnum",
                                    "ligand_id", "ligand_resnum", "ligand_chain",
                                    "residue", "is_cryptic"])
for index, row in df_cryptic_site_residues.iterrows():
    df_res = df_res.append(get_residues(row))

df_res.to_csv("cryptosite_database.csv", index = False)
