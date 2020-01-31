import re
import shutil
import tempfile

import modeller


def get_numbers_from_pdb(pdb_file, chain_id):
    """Get an ordered list of the residue numbers of a single chain of a PDB file.

    Parameters
    ----------
    pdb_file : string
        The location of the pdb file.
    chain_id : string
        The chain of interest.

    Returns
    -------
    residue_numbers : list
        Each entry is a string-typed residue number.  If there is an insertion code,
        this is included.  The list is in the same order as the PDB file.  HETATMS MSE,
        MEX, and ABU are included; other HETATMS are ignored.  This matches MODELLER's
        behavior.

    Warnings
    --------
    This function assumes that all chain IDs in pdb_file are 1 letter.  If there are any
    2-letter chains, the code may fail.  (This is true even in cases where chain_id is
    1 letter but another chain has 2 letters.)
        The code may fail if MEX included; ex. PDB ID 3OW6.  This may also be true of
    ABU.
    """

    residue_numbers = []
    with open(pdb_file, "r") as pdb_opened:
        for line in pdb_opened.readlines():
            is_normal_residue = ((len(line) >= 21) and (line[0:4] == "ATOM") and
                                 (line[21] == chain_id))
            is_hetatm_residue = ((len(line) >= 21) and (line[0:6] == "HETATM") and
                                 (line[21] == chain_id) and
                                 (line[17:20] in ["MSE", "MEX", "ABU"]))
            if is_normal_residue or is_hetatm_residue:
                residue_num = line[22:27].strip()
                if residue_num not in residue_numbers:
                    residue_numbers.append(residue_num)
    return residue_numbers


def align_res_nums(key_pdb_file, key_chain_id, value_pdb_file, value_chain_id):
    """Determine which residues in one PDB file correspond to which in another PDB file.

    Parameters
    ----------
    key_pdb_file : string
        The location of the pdb file whose residue numbers will be keys in the
        returned dictionary.
    key_chain_id : string
        The chain of key_pdb_file that will be aligned.
    value_pdb_file : string
        The location of the pdb file whose residue numbers will be values in the
        returned dictionary.
    value_chain_id : string
        The chain of value_pdb_file that will be aligned.

    Returns
    -------
    dict_residue_nums : dictionary{string : string}
        The keys and values are string-typed residue numbers (from key_pdb_file and
        value_pdb_file).  Any residues that are missing from value_pdb_file
        will be assigned the value "NA".  If any residues in key_pdb_file are
        classified as HETATMs, then they will only included in dict_residue_nums if they
        are MSE, MEX, or ABU.  This matches MODELLER's behavior.
    """

    # A temporary directory to store the output of Modeller's alignment.
    temp_dir_path = tempfile.mkdtemp()
    env = modeller.environ()
    aln = modeller.alignment(env)
    key_model = modeller.model(env, file=key_pdb_file,
                               model_segment=("FIRST:%s" %(key_chain_id),
                                              "LAST:%s" %(key_chain_id)))
    aln.append_model(key_model, atom_files=key_pdb_file,
                     align_codes="key%s" %(key_chain_id))
    value_model = modeller.model(env, file=value_pdb_file,
                                 model_segment=("FIRST:%s" %(value_chain_id),
                                                "LAST:%s" %(value_chain_id)))
    aln.append_model(value_model, atom_files=value_pdb_file,
                     align_codes="value%s" %(value_chain_id))
    aln.salign()
    salign_out_loc = temp_dir_path + "key%s_value%s_salign_output.ali" %(key_chain_id,
                                                                         value_chain_id)
    aln.write(file=salign_out_loc, alignment_format="PIR")
    with open(salign_out_loc, "r") as alignment_opened:
        alignment_lines = alignment_opened.readlines()
        # Ignore the header lines.  The format requires a 2-line header; there may be a
        # blank line before this.
        if alignment_lines[0][0] == ">":
            line_index = 2
        else:
            line_index = 3
        key_sequence_aligned = ""
        while True:
            next_line = alignment_lines[line_index].strip()
            key_sequence_aligned += next_line
            if next_line[len(next_line)-1] == "*":
                key_sequence_aligned = key_sequence_aligned[:-1]
                break
            line_index += 1
        if alignment_lines[line_index+1][0] == ">":
            line_index += 3
        else:
            line_index += 4
        value_sequence_aligned = ""
        while True:
            next_line = alignment_lines[line_index].strip()
            value_sequence_aligned += next_line
            if next_line[len(next_line)-1] == "*":
                value_sequence_aligned = value_sequence_aligned[:-1]
                break
            line_index += 1
    shutil.rmtree(temp_dir_path)
    key_pdb_res_numbers = get_numbers_from_pdb(key_pdb_file, key_chain_id)
    value_pdb_res_numbers = get_numbers_from_pdb(value_pdb_file, value_chain_id)
    dict_residue_nums = {}
    # value_residues_passed is incremented whenever the iteration reaches a spot in the
    # alignment where the value sequence has a residue.
    value_residues_passed = 0
    key_residues_passed = 0
    for i in range(len(value_sequence_aligned)):
        # If both key_sequence_aligned and value_sequence_aligned have residues at
        # the position, then add a dictionary entry mapping the residue number in key
        # to the residue number in value.
        if (key_sequence_aligned[i] != "-") and (value_sequence_aligned[i] != "-"):
            current_key_resnum = key_pdb_res_numbers[key_residues_passed]
            current_value_resnum = value_pdb_res_numbers[value_residues_passed]
            dict_residue_nums[current_key_resnum] = current_value_resnum
            value_residues_passed += 1
            key_residues_passed += 1
        # If key_sequence_aligned has a residue where value_sequence_aligned has a gap,
        # then create a dictionary entry with value NA.
        elif (key_sequence_aligned[i] != "-") and (value_sequence_aligned[i] == "-"):
            dict_residue_nums[key_pdb_res_numbers[key_residues_passed]] = "NA"
            key_residues_passed += 1
        # If key_sequence_aligned has a gap where value_sequence_aligned has a residue,
        # then don't add a dictionary entry.
        elif (key_sequence_aligned[i] == "-") and (value_sequence_aligned[i] != "-"):
            value_residues_passed += 1
    return dict_residue_nums
