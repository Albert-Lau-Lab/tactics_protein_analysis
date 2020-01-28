"""This script should be used in step 5 of the procedure for regenerating the
Cryptosite database.  It reads apo_pdb_and_chain.csv, holo_pdb_and_chain.csv,
and ligands.csv.  It generates pdbs_and_ligands.csv."""

import pandas as pd

data = pd.read_csv("apo_pdb_and_chain.csv")
holo_pdbs = pd.read_csv("holo_pdb_and_chain.csv")
data["holo_pdb_id"] = holo_pdbs["holo_pdb_id"]
data["holo_chain"] = holo_pdbs["holo_chain"]

ligands = pd.read_csv("ligands.csv")
data["ligand_id"] = ligands

data.to_csv("pdbs_and_ligands.csv", index = False)
