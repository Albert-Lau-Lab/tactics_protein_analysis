"""This script should be used in step 1 of the procedure for extending the
Cryptosite database.  If a timeout error occurs, run the script again."""

import os
import shutil
import time
import pandas as pd

from get_pdbs import download_similar_pdbs

output_dir = "extended_db"
if os.path.isdir(output_dir):
    shutil.rmtree(output_dir)
os.mkdir(output_dir)

df_apo_prots = pd.read_csv("../gen_crypto_database/apo_pdb_and_chain.csv")
for index, row in df_apo_prots.iterrows():
    pdb_id = row["apo_pdb_id"].lower()
    chain_id = row["apo_chain"]
    download_dir_fastas = "%s/%s_download_fastas" %(output_dir, pdb_id)
    download_dir_pdbs = "%s/%s_download_pdbs" %(output_dir, pdb_id)
    csv_loc = "%s/%s_similar_prots.csv" %(output_dir, pdb_id)
    download_similar_pdbs(pdb_id, chain_id, download_dir_fastas, download_dir_pdbs, csv_loc)
    time.sleep(1)
