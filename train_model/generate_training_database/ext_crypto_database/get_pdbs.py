import os
import shutil
import xml.etree.ElementTree as ET

import requests
from requests.exceptions import ConnectionError


class PDBProt:
    '''
    A simple class to store which chain of a PDB is of interest.

    Parameters
    ----------
    pdb_id : string
        The lowercase PDB id of the protein.
    chain_of_interest : string
        The chain to be examined.

    Attributes
    ----------
    pdb_id : string
        The lowercase PDB id of the protein.
    chain_of_interest : string
        The chain to be examined.
    '''

    def __init__(self, pdb_id, chain_of_interest):
        self.pdb_id = pdb_id
        self.chain_of_interest = chain_of_interest


    def download_pdb_to_loc(self, loc):
        '''Download the PDB file to a specified location.

        Parameters
        ----------
        loc : string
            The location of the PDB file to be created.  It should include the path
            and name of the file.

        Warnings
        --------
        If the PDB is too large, then it won't be downloaded.  Instead, a HTML error
        message will be downloaded.
        '''

        download_url = "https://files.rcsb.org/download/%s.pdb" %(self.pdb_id)
        try:
            pdb_string = requests.get(download_url, timeout=(9.05, 27))
            with open(loc, "w") as file_opened:
                file_opened.write(pdb_string.text)
        except ConnectionError:
            print("Retrying download after failure")
            pdb_string = requests.get(download_url, timeout=(9.05, 27))
            with open(loc, "w") as file_opened:
                file_opened.write(pdb_string.text)



    def download_fasta_to_loc(self, loc):
        '''Download the FASTA file to a specified location.

        Parameters
        ----------
        loc : string
            The location of the FASTA file to be created.  It should include the path
            and name of the file.
        '''

        download_url = ("https://www.rcsb.org/pdb/download/downloadFastaFiles.do?"
                        "structureIdList=%s&compressionType=uncompressed"
                        %(self.pdb_id))
        try:
            fasta_string = requests.get(download_url, timeout=(9.05, 27))
            with open(loc, "w") as file_opened:
                file_opened.write(fasta_string.text)
        except ConnectionError:
            print("Retrying download after failure")
            fasta_string = requests.get(download_url, timeout=(9.05, 27))
            with open(loc, "w") as file_opened:
                file_opened.write(fasta_string.text)


def get_similar_pdbs(pdb_id, chain_id):
    """Get a list of PDBs with 95% sequence identity to a given PDB.

    Parameters
    ----------
    pdb_id : string
        The lowercase PDB id of the protein.
    chain_id : string
        The chain of interest.

    Returns
    -------
    similar_pdbs : list
        A string containing PDBProt objects for each protein with at least 95% sequence
        identity to pdb_id.  Note that pdb_id itself will have an entry.  If the PDB ID
        3ow6 would be included in similar_pdbs, it is removed.  This is because the
        structure's MEX heteroatom causes Modeller to crash.
    """

    r = requests.get("https://www.rcsb.org/pdb/rest/sequenceCluster?cluster=95"
                     "&structureId=%s.%s" %(pdb_id, chain_id))
    root = ET.fromstring(r.text)
    similar_pdbs = []
    for child in root:
        # child.attrib is a dictionary; "name" is a key.  The corresponding value is a
        # PDB id of the form 1KSZ.A
        similar_pdb_id = child.attrib["name"][0:4].lower()
        similar_pdb_chain = child.attrib["name"][5:]
        # Some PDBs (ex. 4V8Q) have 2-letter chain IDs.  This breaks some of my later
        # code; I don't think that 2-letter chains are part of the official PDB
        # specification.  To make my code simple, I ignore these PDBs.
        if len(similar_pdb_chain) == 1:
            if similar_pdb_id.lower() != "3ow6":
                similar_pdbs.append(PDBProt(similar_pdb_id, similar_pdb_chain))
    return similar_pdbs

def download_similar_pdbs(pdb_id, chain_id, fasta_download_dir, pdb_download_dir,
                          csv_loc):
    """Download the PDB and FASTA files of proteins with 95% identity to a protein.

    Parameters
    ----------
    pdb_id : string
        The lowercase PDB id of the protein.
    chain_id : string
        The chain of interest.
    fasta_download_dir : string
        The directory where the FASTA files should be downloaded.  If the directory
        doesn't exist, it will be created.  If it does exist, its contents will be
        replaced.
    pdb_download_dir : string
        The directory where the PDB files should be downloaded.  If the directory
        doesn't exist, it will be created.  If it does exist, its contents will be
        replaced.
    csv_loc : string
        The location where a CSV file should be written.  The file will list each
        protein that has been downloaded, along with the chain that is similar to
        the chain_id of protein pdb_id.
    """

    print("Downloading PDB and FASTA files for proteins with 95% identity to", pdb_id)
    if os.path.isdir(pdb_download_dir):
        shutil.rmtree(pdb_download_dir)
    os.mkdir(pdb_download_dir)
    if os.path.isdir(fasta_download_dir):
        shutil.rmtree(fasta_download_dir)
    os.mkdir(fasta_download_dir)
    similar_pdbs = get_similar_pdbs(pdb_id, chain_id)
    with open(csv_loc, "w") as csv_opened:
        csv_opened.write("pdb_id,chain_id\n")
        for similar_pdb in similar_pdbs:
            pdb_loc = "%s/%s.pdb" %(pdb_download_dir, similar_pdb.pdb_id)
            similar_pdb.download_pdb_to_loc(pdb_loc)
            # Large PDB files can't be downloaded.  When the code encounters one of
            # these PDBs, an HTML error message will be downloaded instead.  Check if
            # this has occurred.
            with open(pdb_loc, "r") as pdb_opened:
                first_line = pdb_opened.readline()
            if "<!DOCTYPE HTML" in first_line:
                os.remove(pdb_loc)
            else:
                similar_pdb.download_fasta_to_loc("%s/%s.pdb" %(fasta_download_dir,
                                                  similar_pdb.pdb_id))
                csv_opened.write("%s,%s\n" %(similar_pdb.pdb_id,
                                             similar_pdb.chain_of_interest))



def download_list_of_pdbs(pdb_list, fasta_download_dir, pdb_download_dir,
                          csv_loc):
    """Download the PDB and FASTA files of proteins.

    Parameters
    ----------
    pdb_list : list
        Each entry should be of the form pdbid_chain
    fasta_download_dir : string
        The directory where the FASTA files should be downloaded.  If the directory
        doesn't exist, it will be created.  If it does exist, its contents will be
        replaced.
    pdb_download_dir : string
        The directory where the PDB files should be downloaded.  If the directory
        doesn't exist, it will be created.  If it does exist, its contents will be
        replaced.
    csv_loc : string
        The location where a CSV file should be written.  The file will list each
        protein that has been downloaded, along with the chain that is similar to
        the chain_id of protein pdb_id.
    """

    if os.path.isdir(pdb_download_dir):
        shutil.rmtree(pdb_download_dir)
    os.mkdir(pdb_download_dir)
    if os.path.isdir(fasta_download_dir):
        shutil.rmtree(fasta_download_dir)
    os.mkdir(fasta_download_dir)
    similar_pdbs = []
    for pdb_and_chain in pdb_list:
        pdb_and_chain_split = pdb_and_chain.split("_")
        pdb_id = pdb_and_chain_split[0]
        chain = pdb_and_chain_split[1]
        pdb_prot = PDBProt(pdb_id, chain)
        pdb_loc = "%s/%s.pdb" %(pdb_download_dir, pdb_id)
        pdb_prot.download_pdb_to_loc(pdb_loc)
    with open(csv_loc, "w") as csv_opened:
        csv_opened.write("pdb_id,chain_id\n")
        for similar_pdb in similar_pdbs:
            pdb_loc = "%s/%s.pdb" %(pdb_download_dir, similar_pdb.pdb_id)
            similar_pdb.download_pdb_to_loc(pdb_loc)
            # Large PDB files can't be downloaded.  When the code encounters one of
            # these PDBs, an HTML error message will be downloaded instead.  Check if
            # this has occurred.
            with open(pdb_loc, "r") as pdb_opened:
                first_line = pdb_opened.readline()
            if "<!DOCTYPE HTML" in first_line:
                os.remove(pdb_loc)
            else:
                similar_pdb.download_fasta_to_loc("%s/%s.pdb" %(fasta_download_dir,
                                                  similar_pdb.pdb_id))
                csv_opened.write("%s,%s\n" %(similar_pdb.pdb_id,
                                             similar_pdb.chain_of_interest))


