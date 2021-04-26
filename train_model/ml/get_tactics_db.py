import re

with open("train_model.ipynb", "r") as notebook_file:
    notebook_lines = notebook_file.readlines()
dict_holo_to_apos = {}
for line in notebook_lines:
    re_str = ' +"num_passed \d+ args (.*.pdb) ([A-Z]) (.*.pdb) ([A-Z])'
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


with open("database_prots.csv", "w") as csv_file:
    csv_file.write("holoid_chain,apoid_chain\n")
    for key, val in dict_holo_to_apos.items():
        csv_file.write("%s,%s\n" %(key, val))
        print(key, val.count("_"))
