"""If a timeout error occurs, run the script again."""

import os
import shutil
import time
import pandas as pd

from get_pdbs import download_list_of_pdbs

output_dir = "extended_db"
if os.path.isdir(output_dir):
    shutil.rmtree(output_dir)
os.mkdir(output_dir)

df_of_ext_apos = pd.read_csv("../../ml/database_prots.csv")
df_of_crypto_prots = pd.read_csv("../gen_crypto_database/pdbs_and_ligands.csv")
for index, row in df_of_ext_apos.iterrows():
    holo_id_and_chain = row["holoid_chain"].split("_")
    holo_id = holo_id_and_chain[0].lower()
    holo_chain = holo_id_and_chain[1]
    # df_of_ext_apos doesn't have apo ID; get it from df_of_crypto_prots.
    for crypto_index, crypto_row in df_of_crypto_prots.iterrows():
        row_holo_pdb_id = crypto_row["holo_pdb_id"].lower()
        row_holo_chain = crypto_row["holo_chain"]
        if (holo_id == row_holo_pdb_id) and (holo_chain == row_holo_chain):
            apo_pdb_id = crypto_row["apo_pdb_id"].lower()
            apo_chain = crypto_row["apo_chain"]
            break
    print("Downloading PDBS for cryptosite apo %s_%s" %(apo_pdb_id, apo_chain))
    apo_pdb_list = row["apoid_chain"].split()
    download_dir_fastas = "%s/%s_download_fastas" %(output_dir, apo_pdb_id)
    download_dir_pdbs = "%s/%s_download_pdbs" %(output_dir, apo_pdb_id)
    csv_loc = "%s/%s_similar_prots.csv" %(output_dir, apo_pdb_id)
    download_list_of_pdbs(apo_pdb_list, download_dir_fastas, download_dir_pdbs,
                          csv_loc) 
    time.sleep(1)



