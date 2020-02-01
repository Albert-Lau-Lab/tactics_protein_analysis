"""This script should be used in step 2 of the procedure for extending the
Cryptosite database."""

import os
import shutil

import pandas as pd

from get_extended_site import get_extended_site
from check_if_site_unbound import check_if_site_unbound


df_prots_loc = ("../gen_crypto_database/cryptic_site_locations.csv")
df_prots = pd.read_csv(df_prots_loc)

# Some proteins have multiple cryptic sites included in the Cryptosite
# database.  The script classifies a structure as "bad" if any of the sites in
# the database has missing residues or bound ligand.  To accomplish this, the
# script first splits df_prots (which has one entry per protein) into df_sites
# (containing 1 entry per site).  It then classifies structures as "good" or
# "bad" for each site.  It then makes a final classification; a structure is
# only "good" if it is "good" at all of its sites.

# Create df_sites.
list_of_sites = []
for index, row in df_prots.iterrows():
    apo_pdb_id = row["apo_pdb_id"].lower()
    holo_pdb_id = row["holo_pdb_id"].lower()
    holo_pdb_loc = ("../gen_crypto_database/holo_structures/%s.pdb" %(holo_pdb_id))
    holo_chain_id = row["holo_chain"]
    ligand_resn = row["ligand_id"]
    ligand_resi = row["ligand_resnum"]
    ligand_chain = row["ligand_chain"]
    if "/" in ligand_resn:
        ligand_resns = ligand_resn.split("/")
        ligand_resis = ligand_resi.split("/")
        ligand_chains = ligand_chain.split("/")
        for i in range(len(ligand_resns)):
            list_of_sites.append([apo_pdb_id, holo_pdb_id, holo_chain_id, ligand_resns[i], ligand_resis[i], ligand_chains[i]])
    else:
        list_of_sites.append([apo_pdb_id, holo_pdb_id, holo_chain_id, ligand_resn, ligand_resi, ligand_chain])

df_sites = pd.DataFrame(list_of_sites, columns =["apo_pdb_id", "holo_pdb_id", "holo_chain", "ligand_id", "ligand_resnum", "ligand_chain"])

# Iterate over each site, classifying the structure as "good" or "bad" at that
# site.
if os.path.isdir("extended_db/single_site_lists"):
    shutil.rmtree("extended_db/single_site_lists")
os.mkdir("extended_db/single_site_lists")

for index, row in df_sites.iterrows():
    apo_pdb_id = row["apo_pdb_id"].lower()
    holo_pdb_id = row["holo_pdb_id"].lower()
    holo_pdb_loc = ("../gen_crypto_database/holo_structures/%s.pdb" %(holo_pdb_id))
    holo_chain_id = row["holo_chain"]
    ligand_resn = row["ligand_id"]
    ligand_resi = row["ligand_resnum"]
    ligand_chain = row["ligand_chain"]
    site_chain = row["holo_chain"]
    ref_extended_site = get_extended_site(holo_pdb_loc, ligand_resn, ligand_resi, ligand_chain,
                                          site_chain)

    similar_prots_loc = "extended_db/%s_download_pdbs" %(apo_pdb_id)
    similar_prots_list_loc = "extended_db/%s_similar_prots.csv" %(apo_pdb_id)
    with open(similar_prots_list_loc, "r") as similar_prots_list_file:
        similar_prots_list_lines = similar_prots_list_file.readlines()
    good_list_loc = "extended_db/single_site_lists/%s_%s_%s_%s_good_similar_prots.csv" %(apo_pdb_id, ligand_resn, ligand_resi, ligand_chain)
    bad_list_loc = "extended_db/single_site_lists/%s_%s_%s_%s_bad_similar_prots.csv" %(apo_pdb_id, ligand_resn, ligand_resi, ligand_chain)
    with open(good_list_loc, "w") as good_list:
        good_list.write("pdb_id,chain_id\n")
        with open(bad_list_loc, "w") as bad_list:
            bad_list.write("pdb_id,chain_id\n")
            holos = []
            for line in similar_prots_list_lines:
                line = line.strip()
                if line != "pdb_id,chain_id":
                    pdb_of_interest_id = line[0:4]
                    pdb_of_interest_loc = (similar_prots_loc + "/" +
                                           pdb_of_interest_id + ".pdb")
                    pdb_of_interest_chain_id = line[5:]
                    is_apo = check_if_site_unbound(pdb_of_interest_loc, pdb_of_interest_chain_id,
                                       holo_pdb_loc, holo_chain_id, ref_extended_site,
                                       ligand_resn, ligand_resi)
                    if is_apo:
                        good_list.write("%s,%s\n" %(pdb_of_interest_id,
                                                    pdb_of_interest_chain_id))
                    else:
                        bad_list.write("%s,%s\n" %(pdb_of_interest_id,
                                                   pdb_of_interest_chain_id))

# Make final classifications based on whether structures are "good" at all
# sites.
for index, row in df_prots.iterrows():
    apo_pdb_id = row["apo_pdb_id"].lower()
    holo_pdb_id = row["holo_pdb_id"].lower()
    holo_chain_id = row["holo_chain"]
    ligand_resn = row["ligand_id"]
    ligand_resi = row["ligand_resnum"]
    ligand_chain = row["ligand_chain"]
    if "/" in ligand_resn:
        ligand_resns = ligand_resn.split("/")
        ligand_resis = ligand_resi.split("/")
        ligand_chains = ligand_chain.split("/")
        pdbs_in_a_good_list = []
        pdbs_in_a_bad_list = []
        for i in range(len(ligand_resns)):
            ligand_resn = ligand_resns[i]
            ligand_resi = ligand_resis[i]
            ligand_chain = ligand_chains[i]
            good_list_loc = "extended_db/single_site_lists/%s_%s_%s_%s_good_similar_prots.csv" %(apo_pdb_id, ligand_resn, ligand_resi, ligand_chain)
            bad_list_loc = "extended_db/single_site_lists/%s_%s_%s_%s_bad_similar_prots.csv" %(apo_pdb_id, ligand_resn, ligand_resi, ligand_chain)
            with open(good_list_loc, "r") as good_list:
                for line in good_list.readlines():
                    if line.strip() != "pdb_id,chain_id" and line.strip() not in pdbs_in_a_good_list:
                        pdbs_in_a_good_list.append(line.strip())
            with open(bad_list_loc, "r") as bad_list:
                for line in bad_list.readlines():
                    if line.strip() != "pdb_id,chain_id" and line.strip() not in pdbs_in_a_bad_list:
                        pdbs_in_a_bad_list.append(line.strip())
        with open("extended_db/%s_good_similar_prots.csv" %(apo_pdb_id), "w") as final_good_list:
            final_good_list.write("pdb_id,chain_id\n")
            for pdb in pdbs_in_a_good_list:
                # The first condition gets rid of the newline at the end of files.
                if (pdb.strip() != "") and (pdb not in pdbs_in_a_bad_list):
                    final_good_list.write("%s\n" %(pdb))
        with open("extended_db/%s_bad_similar_prots.csv" %(apo_pdb_id), "w") as final_bad_list:
            final_bad_list.write("pdb_id,chain_id\n")
            for pdb in pdbs_in_a_bad_list:
                final_bad_list.write("%s\n" %(pdb))
    else:
        old_good_list_loc = "extended_db/single_site_lists/%s_%s_%s_%s_good_similar_prots.csv" %(apo_pdb_id, ligand_resn, ligand_resi, ligand_chain)
        old_bad_list_loc = "extended_db/single_site_lists/%s_%s_%s_%s_bad_similar_prots.csv" %(apo_pdb_id, ligand_resn, ligand_resi, ligand_chain)
        new_good_list_loc = "extended_db/%s_good_similar_prots.csv" %(apo_pdb_id)
        new_bad_list_loc = "extended_db/%s_bad_similar_prots.csv" %(apo_pdb_id)
        shutil.copyfile(old_good_list_loc, new_good_list_loc)
        shutil.copyfile(old_bad_list_loc, new_bad_list_loc)
