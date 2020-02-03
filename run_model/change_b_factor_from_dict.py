def change_b_factor_from_dict(orig_pdb_loc, new_b_factor_dict, out_pdb_loc):
    """Replace the old b-factor column (if it exists) with new values.

    Parameters
    ----------
    orig_pdb_loc : string
        The location of the original PDB file.  The code will not modify this file; it
        creates a new output file.  The file must have an "occupancy" column so that the
        ATOM lines are at least 60 characters long.  It doesn't need to have a b-factor
        column.  It shouldn't have any HETATM lines or multiple models.
    new_b_factor_dict : dictionary string:number
        A dictionary containing the new b-factors.  The key is a string of the form
        resnum:chain.  The value is the b-factor for that residue.  If orig_pdb_loc contains
        residues not found in new_b_factor_dict, then the b-factors for those residues will be
        assumed to be 0.  Each b-factor will be truncated to 6 characters.  So passing
        the number 1234567 will cause problems; the number will become 123456.
    out_pdb_loc : string
        The location of the output file that will be created.  If this file already
        exists, then it will be overwritten.

    Returns
    -------
    None
    """

    with open(orig_pdb_loc, "r") as orig_pdb_file:
        orig_pdb_lines = orig_pdb_file.readlines()
    changed_lines = []
    for line in orig_pdb_lines:
        if (len(line.strip()) >= 60) and (line[0:4] == "ATOM"):
            # The b-factor should be exactly 6 characters.  If there are less than 6
            # characters of numbers, then the number should be right-justified with
            # spaces added so that the total length is 6.
            # The code b_factor[:min(6, len(b_factor))] limits the string to at most 6
            # charcters.  The code {:>6}'.format(arg) right-justifies (because of ">")
            # and pads with spaces to length 6.
            resnum = line[22:27].strip()
            chain = line[21]
            resnum_and_chain = "%s:%s" %(resnum, chain)
            if resnum_and_chain in new_b_factor_dict:
                b_factor = str(new_b_factor_dict[resnum_and_chain])
            else:
                b_factor = str(0)
            b_factor_fit = '{:>6}'.format(b_factor[:min(6, len(b_factor))])
            changed_line = line[0 : 60] + b_factor_fit
            if len(line) >= 67:
                changed_line += line[66 : len(line)].strip() # Remove the newline.
            changed_lines.append(changed_line)
    with open(out_pdb_loc, "w") as out_pdb_file:
        for line in changed_lines:
            out_pdb_file.write("%s\n" %(line))
