import os
import copy
import __main__
__main__.pymol_argv = ['pymol', '-qc'] # Pymol: quiet and no GUI
import pymol
import numpy as np

pymol.finish_launching()


def get_extended_site(holo_pdb_loc, ligand_resn, ligand_resi, ligand_chain, site_chain):
    """Determine which residues are within 9 Angstroms of the ligand's centroid.

    Parameters
    ----------
    holo_pdb_loc : string
        The location of the pdb file.
    ligand_resn : string
        The name of the ligand.
    ligand_resi : string
        The residue index of the ligand.
    ligand_chain : string
        The chain of the ligand.
    site_chain : string
        The protein chain containing the site.

    Returns
    -------
    extended_site_list : list
        A list of the residue indices of all residues containing an atom within 9
        Angstroms of the ligand's centroid.  Note that this list only includes protein
        residues in chain site_chain.  Also note that the returned list doesn't store
        the value of site_chain.
    """

    print("getting extended site for", holo_pdb_loc, ligand_resn, ligand_resi, ligand_chain, site_chain)
    pymol.cmd.reinitialize()
    pymol.cmd.load(holo_pdb_loc)
    # Select the ligand.  Find its centroid.
    lig_sel_string = ("resn %s and resi %s and chain %s" %(ligand_resn, ligand_resi, ligand_chain))
    pymol.cmd.select("ligand", lig_sel_string)
    lig_coords = pymol.cmd.get_coords("ligand")
    lig_centroid_array = np.mean(lig_coords, axis=0)
    lig_centroid_list = lig_centroid_array.tolist()
    # Create a pseudoatom at the centroid of the ligand.  Find all residues with at
    # least 1 atom within 9 angstroms of the centroid.
    pymol.cmd.pseudoatom("lig_centroid_pseudoatom", pos=lig_centroid_list)
    # "byres (all within 9 of (lig_centroid_pseudoatom))" selects all residues
    # containing an atom within 9 Anstroms of the centroid.
    # "byres name ca" gets rid of non-protein residues (ex. water).
    extended_site_sel_string = ("chain %s and byres name ca and "
                                "byres (all within 9 of "
                                "(lig_centroid_pseudoatom))" %(site_chain))
    pymol.cmd.select("extended_site_all", extended_site_sel_string)
    pymol.cmd.select("extended_site_ca", "extended_site_all and name ca")
    pymol.stored.extended_site_list = []
    pymol.cmd.iterate("extended_site_ca",
                      "pymol.stored.extended_site_list.append(resi)")
    # I don't know if copying the list is necessary.  But I did it because I don't
    # want to risk the garbage collector doing anything unexpected.
    return copy.deepcopy(pymol.stored.extended_site_list)


