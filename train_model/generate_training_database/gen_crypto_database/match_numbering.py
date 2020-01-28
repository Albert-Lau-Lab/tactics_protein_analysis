"""This script should be used in step 12 of the procedure for regenerating the
Cryptosite database.  It reads cryptic_site_locations.csv.  It generates the
directory apo_holo_numbering_dicts, which contains json files matching residue
numbers between apo and holo structures."""

import re
import json
import os
import shutil
from string import Template

import pandas as pd
import modeller


def get_chain_seq_from_fasta(fasta_file, chain_id):
    with open(fasta_file, "r") as fasta_file_opened:
        reading_chain_of_interest = False # Changed to True when the correct header is read.
        sequence = "" # Initialization
        for line in fasta_file_opened.readlines():
            if (len(line) >= 1) and (line[0] == ">"):
                re_string_for_header = ">[A-Za-z0-9]{4}:([A-Za-z])"
                re_match_for_header = re.match(re_string_for_header, line)
                if re_match_for_header == None: # If the header is incorrectly formatted.
                    print("Error: FASTA file %s has incorrectly formatted header." %(fasta_file))
                    exit()
                elif re_match_for_header.groups()[0] == chain_id:
                    reading_chain_of_interest = True
                elif reading_chain_of_interest == True: # If the script has just finished reading the chain of interest.
                    break
            elif reading_chain_of_interest == True:
                sequence += line.strip()
    return sequence


def get_numbers_from_pdb(pdb_file, chain_id):
    residue_numbers = []
    with open(pdb_file, "r") as pdb_opened:
        for line in pdb_opened.readlines():
            if (len(line) >= 21) and (line[0:4] == "ATOM") and (line[21] == chain_id):
                residue_num = line[22:27].strip()
                if residue_num not in residue_numbers:
                    residue_numbers.append(residue_num)
    return residue_numbers

def align_res_nums(apo_pdb_file, apo_pdb_id, apo_chain_id, holo_pdb_file, holo_pdb_id, holo_chain_id):
    env = modeller.environ()
    aln = modeller.alignment(env)
    apo_model = modeller.model(env, file = apo_pdb_file, model_segment=("FIRST:%s" %(apo_chain_id), "LAST:%s" %(apo_chain_id)))
    aln.append_model(apo_model, atom_files = apo_pdb_id, align_codes = "%s%s" %(apo_pdb_id, apo_chain_id))
    holo_model = modeller.model(env, file = holo_pdb_file, model_segment=("FIRST:%s" %(holo_chain_id), "LAST:%s" %(holo_chain_id)))
    aln.append_model(holo_model, atom_files = holo_pdb_id, align_codes = "%s%s" %(holo_pdb_id, holo_chain_id))
    aln.salign()
    alignment_filename = "%s%s_%s%s_salign_output.ali" %(apo_pdb_id, apo_chain_id, holo_pdb_id, holo_chain_id)
    aln.write(file=alignment_filename, alignment_format="PIR")
    with open(alignment_filename, "r") as alignment_opened:
        alignment_lines = alignment_opened.readlines()
        # Ignore the header lines.  The format requires a 2-line header; there may be a blank line before this.
        if alignment_lines[0][0] == ">":
            line_index = 2
        else:
            line_index = 3
        apo_sequence_aligned = ""
        while True:
            next_line = alignment_lines[line_index].strip()
            apo_sequence_aligned += next_line
            if next_line[len(next_line)-1] == "*":
                apo_sequence_aligned = apo_sequence_aligned[:-1]
                break
            line_index += 1
        if alignment_lines[line_index+1][0] == ">":
            line_index += 3
        else:
            line_index += 4
        holo_sequence_aligned = ""
        while True:
            next_line = alignment_lines[line_index].strip()
            holo_sequence_aligned += next_line
            if next_line[len(next_line)-1] == "*":
                holo_sequence_aligned = holo_sequence_aligned[:-1]
                break
            line_index += 1
    os.remove(alignment_filename)
    apo_pdb_res_numbers = get_numbers_from_pdb(apo_pdb_file, apo_chain_id)
    holo_pdb_res_numbers = get_numbers_from_pdb(holo_pdb_file, holo_chain_id)
    dict_key_apo_val_holo = {}
    holo_residues_passed = 0 # incremented whenever the iteration reaches a spot in the alignment where the holo sequence has a residue.
    apo_residues_passed = 0
    for i in range(len(holo_sequence_aligned)):
        if (apo_sequence_aligned[i] != "-") and (holo_sequence_aligned[i] != "-"):
            #print(len(apo_pdb_res_numbers), apo_residues_passed, len(holo_pdb_res_numbers), holo_residues_passed)
            #print(apo_pdb_res_numbers, holo_pdb_res_numbers)
            #print(len(apo_sequence_aligned), len(holo_sequence_aligned), "len")
            #print(apo_sequence_aligned, holo_sequence_aligned)
            dict_key_apo_val_holo[apo_pdb_res_numbers[apo_residues_passed]] = holo_pdb_res_numbers[holo_residues_passed]
            holo_residues_passed += 1
            apo_residues_passed += 1
        elif (apo_sequence_aligned[i] != "-") and (holo_sequence_aligned[i] == "-"):
            dict_key_apo_val_holo[apo_pdb_res_numbers[apo_residues_passed]] = "NA"
            apo_residues_passed += 1
        elif (apo_sequence_aligned[i] == "-") and (holo_sequence_aligned[i] != "-"):
            holo_residues_passed += 1
    print(dict_key_apo_val_holo)
    print(apo_sequence_aligned)
    print(holo_sequence_aligned)
    return dict_key_apo_val_holo

output_directory = "apo_holo_numbering_dicts"
if os.path.exists(output_directory) and os.path.isdir(output_directory):
    shutil.rmtree(output_directory)
os.mkdir(output_directory)
df = pd.read_csv("cryptic_site_locations.csv") # This file is a modified version of the one created by find_cryptic_site.py.
for index, row in df.iterrows():
    holo_pdb_id = row["holo_pdb_id"]
    holo_pdb_file = "holo_structures/%s.pdb" %(holo_pdb_id.lower()) 
    holo_chain_id = row["holo_chain"]
    apo_pdb_id = row["apo_pdb_id"]
    apo_pdb_file = "apo_structures/%s.pdb" %(apo_pdb_id.lower())
    apo_chain_id = row["apo_chain"]
    apo_holo_dict = align_res_nums(apo_pdb_file, apo_pdb_id, apo_chain_id, holo_pdb_file, holo_pdb_id, holo_chain_id)
    with open("%s/%s_%s.json" %(output_directory, apo_pdb_id, holo_pdb_id), "w") as output_file:
        json.dump(apo_holo_dict, output_file)
