def get_all_ca_pos(pdb_loc):
    """Get the position of each residue's alpha carbon.

    Parameters
    ----------
    pdb_file_loc : string
        The path to the pdb file that the function is run on.  The protein's chains
        should be specified in the Chain column.

    Returns
    -------
    ca_pos_dict : dictionary
        Stores the alpha-carbon position for each residue.
        Keys are strings of the form resnum:chain.

    """

    with open(pdb_loc, "r") as pdb_file:
        pdb_file_lines = pdb_file.readlines()
    ca_pos_dict = {}
    for line in pdb_file_lines:
        if ((len(line) >= 21) and (line[0:4] == "ATOM") and (line[13:15] == "CA")):
            x_pos = float(line[30:38])
            y_pos = float(line[38:46])
            z_pos = float(line[46:54])
            resnum = line[22:27].strip()
            chain_id = line[21]
            resnum_and_chain = resnum + ":" + chain_id
            ca_pos_dict[resnum_and_chain] = [x_pos, y_pos, z_pos]
    return ca_pos_dict
