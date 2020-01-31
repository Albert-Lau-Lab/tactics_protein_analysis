import re

import __main__
__main__.pymol_argv = ['pymol', '-qc'] # Pymol: quiet and no GUI
import pymol

from align import align_res_nums


pymol.finish_launching()


def check_if_site_unbound(pdb_of_interest_loc, pdb_of_interest_chain_id,
                          ref_pdb_loc, ref_chain_id, ref_extended_site,
                          ref_ligand_resn, ref_ligand_resi):
    """Check that no ligand is bound to a site & no site residues are missing.

    Parameters
    ----------
    pdb_of_interest_loc : string
        The location of the PDB to be checked.
    pdb_of_interest_chain_id : string
        The chain to be checked.
    ref_pdb_loc : string
        The location of a structure that has a ligand bound at the cryptic
        site.
    ref_chain_id : string
        The chain of the structure at ref_pdb_loc that has the cryptic site.
    ref_extended_site : list of strings
        A list of residue numbers of all residues in ref_chain_id of the
        ref_pdb_loc structure that are within 9 Angstroms of the center of the
        ligand.  Each entry should be a string-typed number; it should not list
        the chain.  This list can be created by the function
        get_extended_site.
    ref_ligand_resn : string
        The name of the ligand in ref_pdb_loc.  It should exactly match the
        name in the file.
    ref_ligand_resi : string
        The string-formatted residue number of the ligand in ref_pdb_loc.


    Returns
    -------
    site_is_unbound : bool
        True if no ligand is present at the site and no residues within 9
        Angstroms of the site are missing.  False if there is a ligand or if
        residues are missing.
    """

    pymol.cmd.reinitialize()
    # Abbreviations: int is pdb_of_interest; ref is ref_pdb.
    # Determine which residues in pdb_of_interest were part of the extended site in the
    # reference structure.
    ref_pdb_to_int_pdb_dict = align_res_nums(ref_pdb_loc, ref_chain_id,
                                             pdb_of_interest_loc,
                                             pdb_of_interest_chain_id)
    int_extended_site = []
    for ref_site_res in ref_extended_site:
        # ref_pdb_to_int_pdb_dict doesn't have any residues that are HETATM in the
        # ref_pdb.  But ref_extended_site has these residues.  I ignore them, because
        # this is simple.
        if ref_site_res in ref_pdb_to_int_pdb_dict:
            int_site_res = ref_pdb_to_int_pdb_dict[ref_site_res]
            if int_site_res == "NA":
                return False
            int_extended_site.append(int_site_res)
    # Align the reference structure's extended site with the same residues in
    # pdb_of_interest.
    pymol.cmd.load(ref_pdb_loc, "reference")
    pymol.cmd.load(pdb_of_interest_loc, "interest")
    # Iteratively create the selection string.  Select the binding-site residues.
    ref_site_sel_string = "reference and chain %s and resi " %(ref_chain_id)
    for ref_site_res in ref_extended_site:
        if ref_site_res in ref_pdb_to_int_pdb_dict: # See above for explanation.
            ref_site_sel_string += "+%s" %(ref_site_res)
    ref_site_sel_string = ref_site_sel_string[:-1] # Remove the trailing + symbol.
    pymol.cmd.select("ref_extended_site", ref_site_sel_string)

    # Select the binding-site residues in the pdb_of_interest.
    int_site_sel_string = "interest and chain %s and resi " %(pdb_of_interest_chain_id)
    for int_site_res in int_extended_site:
        int_site_sel_string += "+%s" %(int_site_res)
    int_site_sel_string = int_site_sel_string[:-1] # Remove the trailing + symbol.
    pymol.cmd.select("int_extended_site", int_site_sel_string)

    # Align the PDBs.  Select the reference structure's ligand.  Check for any ligands
    # (except water and metals) in the pdb_of_interest within 5 Angstroms of the
    # reference structure's ligand.
    pymol.cmd.align("int_extended_site", "ref_extended_site")
    ref_lig_sel_string = ("reference and resn %s and resi %s and "
                          "(byres all within 10 of "
                          "(reference and chain %s and resi %s))"
                          %(ref_ligand_resn, ref_ligand_resi, ref_chain_id,
                            ref_extended_site[0]))
    pymol.cmd.select("ref_lig", ref_lig_sel_string)
    nearby_ligand_sel_string = ("not metal and not (resn HOH) and not polymer.protein "
                                "and (interest within 5 of ref_lig)")
    pymol.cmd.select("int_lig_nearby", nearby_ligand_sel_string)
    
    pymol.stored.num_nearby_lig_atoms = 0
    pymol.cmd.iterate("int_lig_nearby", "pymol.stored.num_nearby_lig_atoms += 1")
    if pymol.stored.num_nearby_lig_atoms > 0:
        site_is_unbound = False
    else:
        site_is_unbound = True
    return site_is_unbound
