def get_list_of_segids(pdb_file_loc):
    with open(pdb_file_loc, "r") as pdb_file_opened:
        pdb_file_lines = pdb_file_opened.readlines()
    segids = []
    for line in pdb_file_lines:
        if (len(line) >= 75) and (line[0:4] == "ATOM"):
            segid = line[72:76].strip()
            if segid not in segids:
                segids.append(segid)
    return segids
