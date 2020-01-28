"""This script should be used in step 6 of the procedure for regenerating the
Cryptosite database.  It reads apo_ids_unformatted.txt and
holo_ids_unformatted.txt.  It uses the data to create
apo_pdbs_formatted_for_downloader.txt and 
holo_pdbs_formatted_for_downloader.txt."""

def reformat(old_file_name, new_file_name):
    ids = ""
    with open(old_file_name, "r") as old_file_opened:
        for line in old_file_opened:
            id_with_chain = line.strip()
            id_without_chain = id_with_chain[:-1]
            ids += "%s," %(id_without_chain)
        ids = ids[:-1] # Remove comma at end.
    with open(new_file_name, "w") as new_file_opened:
        new_file_opened.write(ids)

reformat("apo_ids_unformatted.txt", "apo_pdbs_formatted_for_downloader.txt")
reformat("holo_ids_unformatted.txt", "holo_pdbs_formatted_for_downloader.txt")
