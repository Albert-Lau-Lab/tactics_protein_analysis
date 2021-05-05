import re
import pandas as pd

with open("train_model.ipynb", "r") as notebook_file:
    notebook_lines = notebook_file.readlines()
dict_holo_to_apos = {}
for line in notebook_lines:
    re_str = ' +"num_passed \d+ args (.*.pdb) ([A-Za-z]) (.*.pdb) ([A-Za-z])'
    re_srch = re.search(re_str, line)
    if re_srch is not None:
        apo_id = re_srch.group(1)[-8:-4]
        apo_chain = re_srch.group(2)
        apoid_chain = "%s_%s" %(apo_id, apo_chain)
        holo_id = re_srch.group(3)[-8:-4]
        holo_chain = re_srch.group(4)
        holoid_chain = "%s_%s" %(holo_id, holo_chain)
        if holoid_chain in dict_holo_to_apos:
            dict_holo_to_apos[holoid_chain] += " %s" %(apoid_chain)
        else:
            dict_holo_to_apos[holoid_chain] = apoid_chain
            
with open("extended_database_prots.csv", "w") as csv_file:
    csv_file.write("holoid_chain,apoid_chain\n")
    for key, val in dict_holo_to_apos.items():
        csv_file.write("%s,%s\n" %(key, val))

df_orig = pd.read_csv("../generate_training_database/gen_crypto_database/pdbs_and_ligands.csv")
for index, row in df_orig.iterrows():
    apo_pdb_and_chain = "%s_%s" %(row["apo_pdb_id"].lower(), row["apo_chain"])
    holo_pdb_and_chain = "%s_%s" %(row["holo_pdb_id"].lower(), row["holo_chain"]) 
    if holo_pdb_and_chain in dict_holo_to_apos.keys():
        dict_holo_to_apos[holo_pdb_and_chain] = "%s %s" %(apo_pdb_and_chain, dict_holo_to_apos[holo_pdb_and_chain])
    else:
        dict_holo_to_apos[holo_pdb_and_chain] = apo_pdb_and_chain
with open("all_database_prots.csv", "w") as csv_file:
    csv_file.write("holoid_chain,apoid_chain\n")
    for key, val in dict_holo_to_apos.items():
        csv_file.write("%s,%s\n" %(key, val))
        print(key, val.count("_"))         
