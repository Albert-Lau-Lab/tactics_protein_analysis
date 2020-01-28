"""This script should be used in step 4 of the procedure for regenerating the
Cryptosite database.  It reads apo_ids_unformatted.txt and
holo_ids_unformatted.txt.  It uses the data to create apo_pdb_and_chain.csv
and holo_pdb_and_chain.csv.

The output CSV files have 1 line per cryptic site.  Several proteins have
multiple cryptic sites; thus the output files have a few lines
repeated.  The line repetition is different for apo and holo.  This is because
apo protein 3CJ0 is paired with 2 different holo proteins."""

apo_ids_string = ""
with open("apo_ids_unformatted.txt", "r") as apo_unformatted_file:
    for line in apo_unformatted_file:
        id_with_chain = line.strip()
        id_without_chain = id_with_chain[:-1]
        chain = id_with_chain[-1]
        apo_ids_string += "%s,%s\n" %(id_without_chain, chain)
        # These 3 proteins each have 2 cryptic sites.  They were listed
        # once (in the previous statement); list them again so that they are
        # listed twice.
        if ((id_without_chain == "1G4E") or (id_without_chain == "2IYT") or
                (id_without_chain == "3CJ0")):
            apo_ids_string += "%s,%s\n" %(id_without_chain, chain)
        # This protein has 3 cryptic sites.
        if id_without_chain == "1PKL":
            apo_ids_string += "%s,%s\n" %(id_without_chain, chain)
            apo_ids_string += "%s,%s\n" %(id_without_chain, chain)
with open("apo_pdb_and_chain.csv", "w") as apo_formatted_file:
    apo_formatted_file.write("apo_pdb_id,apo_chain\n")
    apo_formatted_file.write(apo_ids_string)

holo_ids_string = ""
with open("holo_ids_unformatted.txt", "r") as holo_unformatted_file:
    for line in holo_unformatted_file:
        id_with_chain = line.strip()
        id_without_chain = id_with_chain[:-1]
        chain = id_with_chain[-1]
        holo_ids_string += "%s,%s\n" %(id_without_chain, chain)
        # These 2 proteins each have 2 cryptic sites.
        if (id_without_chain == "1G67") or (id_without_chain == "2IYQ"):
            holo_ids_string += "%s,%s\n" %(id_without_chain, chain)
        # This protein has 3 cryptic sites.
        if id_without_chain == "3HQP":
            holo_ids_string += "%s,%s\n" %(id_without_chain, chain)
            holo_ids_string += "%s,%s\n" %(id_without_chain, chain)
with open("holo_pdb_and_chain.csv", "w") as holo_formatted_file:
    holo_formatted_file.write("holo_pdb_id,holo_chain\n")
    holo_formatted_file.write(holo_ids_string)
