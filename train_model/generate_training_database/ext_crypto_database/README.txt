Just like the original CryptoSite database, the extended database is
too big to store on GitHub.  But the list of proteins can be stored,
so users reconstructing the database do not have to start over from
the beginning.

##### How to extend the CryptoSite database using this GitHub Repository     #####
##### (Recommended because it is faster than the alternative below)          #####

* The Jupyter notebook train_model/ml/retrain_model.ipynb downloads the
  extended-database proteins.  So although users reconstructing the database
  will need to run scripts to download the original CryptoSite database proteins,
  the extended database proteins are downloaded automatically when training
  the model.




##### Steps to extend the CryptoSite database from scratch   #####
##### (Not recommended because it involves extra work)       #####


(1) Run the Python script run_get_pdbs.py.  It creates the directory
    extended_db.  Within this directory, it creates 2 directories for each
    Cryptosite apo protein.  It downloads PDBs and FASTAs of proteins
    containing chains with 95% sequence identity to the apo protein; the PDBs
    are stored in one directory and the FASTAs are stored in the other.  It
    creates a CSV file listing the PDB ID and chain ID of each downloaded
    protein.
        * If a timeout error occurs, run the script again.

(2) Run the Python script run_check_pdb.py.  It determines which downloaded
    PDBs should be part of the ML database.  For a protein to be included, it
    must not be missing any residues at/near the cryptic site.  It also must
    not have a ligand bound at the cryptic site.  (The exception to this is
    the set of holo proteins in the original Cryptosite database.)  The script
    creates 2 CSV files for each Cryptosite apo protein.  One lists "good"
    proteins that should be included in the database; the other lists "bad"
    proteins that should not be included.
        * Some proteins have multiple sites included in the Cryptosite
          database.  These proteins are only classified as "good" if they are
          "good" at all sites.
        * In order to classify proteins with multiple sites, the code creates
          a directory named "single_site_lists".  This directory contains
          classifications for each site on each protein (including proteins
          with only one site).
