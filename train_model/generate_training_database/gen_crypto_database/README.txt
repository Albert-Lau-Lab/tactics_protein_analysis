I created a procedure to reconstruct the CryptoSite database.  The reconstructed
database includes the following important files and directories:
* Directories apo_structures and holo_structures.  These contain the downloaded
  PDB files for each database protein.
* Directories apo_seqs and holo_seqs.  These contain the downloaded FASTA
  files for each database protein.  I'm not sure if this data is necessary
  for training the model; it might be possible to train the model without
  downloading the sequences.
* Various csv files with lists of the database proteins; the different csv files
  are in slightly different formats from each other.  A particularly important
  file is cryptosite_database.csv, which lists whether each residue of each protein 
  is part of a cryptic site.

The database's set of PDB files is too big to store on GitHub.  However, the csv files
are small enough that I can include them in this repo.  Users wishing to recreate the CryptoSite
database can start with these csv files, instead of going through the entire
procedure.

##### Steps to recreate the Cryptosite database from  this GitHub Repository #####
##### (Recommended because it is faster than the alternative below)          #####
(1) Download the PDB files for the CryptoSite database proteins:
    (a) Go to https://www.rcsb.org/docs/programmatic-access/batch-downloads-with-shell-script.
        Download the "batch-download script".
    (b) Make a directory (within this directory) called apo_structures.  Copy (cp command; not mv)
        the "batch-download script" and apo_pdbs_formatted_for_downloader.txt into the
        apo_structures directory.
    (c) Run the "batch-download script" using the following command:
            ./batch_download.sh -f apo_pdbs_formatted_for_downloader.txt -p
    (d) Delete the "batch-download script", apo_pdbs_formatted_for_downloader.txt,
        and any other non-pdb files from the apo_structures directory.
    (e) Repeat steps (b), (c), and (d) for holo proteins, using the file
        holo_pdbs_formatted_for_downloader.txt and the directory holo_structures.
    (f) The holo dataset contains the protein 1fqc.  The PDB file underwent
        "remediation" after the CryptoSite database was created, so that the
        version on the PDB website is slightly different from the version used
        to train TACTICS.  Download version 1.2 of the structure from the PDB
        website; replace the downloaded structure in holo_structures with
        version 1.2.  If needed, change the filename so it is the same as
        the download structure's filename.
    (g) Similarly, replace holo structure 2ixu with version 1.4.  Replace
        2eum with version 1.3.
    (h) Run the following command in apo_structures and holo_structures
        to convert the filenames to lowercase:
            for i in $( ls | grep [A-Z] ); do mv -i $i `echo $i | tr 'A-Z' 'a-z'`; done

(2) NOTE: THIS STEP MIGHT NOT BE NECESSARY.
    Similarly to step 7, go to https://www.rcsb.org/downloads/fasta.
    Download the FASTA files into directories apo_seqs
    and holo_seqs.  Select "Individual FASTA Files" and "uncompressed" on the
    webpage.



##### Steps to recreate the Cryptosite database from scratch #####
##### (Not recommended because it involves extra work)       #####
(1) Copy the list of apo PDB IDs on page 25 of the Cryptosite paper's
    supplemental information.  Paste the list into a blank document named
    apo_ids_unformatted.txt.  Add the apo PDBs on page 29 of the Cryptosite
    paper's supplement to this list.  Remove 1MY1 and 1MY0 from the list because the
    AMPA receptor was excluded from the database.  The file should have 91
    lines.

(2) Copy the holo PDB IDs from pages 25 and 29 of the Cryptosite paper's
    supplement.  Paste them into a blank document named
    holo_ids_unformatted.txt.  Make the following changes:
        * One of the lines will be "2BRLA/3FQKB".  Reformat this so that 3FQKB
          is on the line below 2BRLA.  Delete the slash.
        * Remove 1FTL and 1N0T (AMPA receptor).
    The file should have 92 lines.

(3) Create a blank document named ligands.csv.  Add a line with the word
    ligand.  Copy the ligand names from pages 25 and 29 of the Cryptosite
    paper's supplement.  Paste them into ligands.csv.  Reformat so that each
    ligand has its own line and there are no slashes.  Remove line 20 (DNQ)
    and 87 (AT1) because they are the AMPA receptor's ligands.  There should be 97 lines
    (including the header).
        * IMPORTANT: The order of the list matters.  For example, the line
          "ATP/FDP/OXL" should be reformatted so that OXL is below FDP which
          is below ATP.
        * CSV files normally have commas.  But this file only has 1 column, so
          no commas are necessary.

(4) Run the script split_pdb_and_chain.py.  This will read the files
    apo_ids_unformatted.txt and holo_ids_unformatted.txt and generate
    reformatted versions named apo_pdb_and_chain.csv and
    holo_pdb_and_chain.csv.
        * The reformatted versions have 1 line per cryptic site.  Some
          proteins have multiple cryptic sites, so some lines are repeated
          in the output CSV files.

(5) Run the script combine_apo_holo_ligand.py.  This will read the files
    apo_pdb_and_chain.csv, holo_pdb_and_chain.csv, and ligands.csv.  It will
    generate the file pdbs_and_ligands.csv.

(6) Run the script reformat_names.py.  This script reads the files
    apo_ids_unformatted.txt and holo_ids_unformatted.txt.  It creates the
    files apo_pdbs_formatted_for_downloader.txt and
    holo_pdbs_formatted_for_downloader.txt, which are formatted in the way
    that the PDB's downloader expects.

(7) Download the PDB files for the CryptoSite database proteins:
    (a) Go to https://www.rcsb.org/docs/programmatic-access/batch-downloads-with-shell-script.
        Download the "batch-download script".
    (b) Make a directory (within this directory) called apo_structures.  Copy (cp command; not mv)
        the "batch-download script" and apo_pdbs_formatted_for_downloader.txt into the
        apo_structures directory.
    (c) Run the "batch-download script" using the following command:
            ./batch_download.sh -f apo_pdbs_formatted_for_downloader.txt -p
    (d) Delete the "batch-download script", apo_pdbs_formatted_for_downloader.txt,
        and any other non-pdb files from the apo_structures directory.
    (e) Repeat steps (b), (c), and (d) for holo proteins, using the file
        holo_pdbs_formatted_for_downloader.txt and the directory holo_structures.
    (f) The holo dataset contains the protein 1fqc.  The PDB file underwent
        "remediation" after the CryptoSite database was created, so that the
        version on the PDB website is slightly different from the version used
        to train TACTICS.  Download version 1.2 of the structure from the PDB
        website; replace the downloaded structure in holo_structures with
        version 1.2.  If needed, change the filename so it is the same as
        the download structure's filename.
    (g) Similarly, replace holo structure 2ixu with version 1.4.  Replace
        2eum with version 1.3.
    (h) Run the following command in apo_structures and holo_structures
        to convert the filenames to lowercase:
            for i in $( ls | grep [A-Z] ); do mv -i $i `echo $i | tr 'A-Z' 'a-z'`; done

(8) NOTE: THIS STEP MIGHT NOT BE NECESSARY.
    Similarly to step 7, go to https://www.rcsb.org/downloads/fasta.
    Download the FASTA files into directories apo_seqs
    and holo_seqs.  Select "Individual FASTA Files" and "uncompressed" on the
    webpage.

(9) Run the script find_cryptic_site.py.  It creates the file
    cryptic_site_locations.csv.

(10) When cryptic_site_locations.csv is first generated, it has some errors.
     Fix them:
         * Delete the line for the 5-residue site on 1DUB/1EY3.
               REASON: The file has 2 lines for 1DUB.  One line is for a
               5-residue site; the other is for a 25-residue site.  The
               5-residue site isn't listed in the Cryptosite paper's
               supplementary material, but the 25-residue site is listed.  Thus
               the latter site is likely to be correct; the former is likely to
               be incorrect.
         * Delete the line for the 8-residue site on 3PEO/2BYS.
               REASON: It isn't listed in the Cryptosite paper's supplement.
         * Delete the line for the Chain A ligand in 1A8I/2IEG.
               REASON: The file has two 11-residue sites; the correct one is
               almost certainly the one with the Chain B ligand.  There are two
               reasons for this.  Firstly, the PDB file's listing both the
               ligand and the protein as "Chain B" implies that they are bound.
               Secondly, Table S2 of Beglov et al. (2018) lists the minimum
               distance between protein and ligand as 2.55 Angstroms.  This is
               true of the chain B ligand, but not of the chain A ligand.  The
               latter's atom O19 is closer to protein chain A's Lys 191 (atom
               NZ) and is more than 2.5 Angstroms from the nearest chain B
               protein atom.
        * Combine the 2 lines for 2ZB1/2NPQ into a single line with this text:
          2ZB1,A,2NPQ,A,BOG,1000,A, 191  192  195  197  198  199  200  201  232  236  242  246  249  259  291  292  293  294  296 229 233 255 258,23
              REASON: There are 2 ligands that are close to each other in 1PZO.
              Including all residues close to either ligand gives a site with
              23 residues, which is the same count as found in the Cryptosite
              paper's supplement.
        * Combine the 2 lines for 1JWP/1PZO into a single line with this text:
          1JWP,A,1PZO,A,CBT, 300,A, 130  216  217  220  235  236  237  244  245  246  263  276  279  221 224 225 250 261 280  283  284  286,22
              REASON: Similar to 2NBQ, there are 2 ligands near each other.
              Combining the sites gives the correct number of residues.
     When the file is corrected, it should have 97 lines.  The first line is a
     header; there are 96 cryptic sites.  This should be one smaller than the
     database described in the Cryptosite paper.  The way that the paper
     counted sites merits some explantion.
         * The paper mentions a database of 84 cryptic sites.  This is the
           training database; it excludes the 14 proteins used as a test
           set.  Combining the training and test sets gives a database of
           84+14=98 proteins, which is the same size as the reconstructed set.
         * The paper's supplement mentions a database of 79 proteins.  This is
           the number of proteins in the training set.  Several proteins have
           multiple cryptic sites; thus there are 84 cryptic sites but only 79
           proteins in the training set.

(11) Even though cryptic_site_locations.csv is now correct, it needs more
     reformatting before it can be used.  The issue is that some apo/holo
     pairs have multiple cryptic sites.  Those pairs are listed multiple times
     (once per cryptic site).  Combine all sites for each protein into 1 line
     per protein:
         * Delete both lines for 1G4E/1G67 and replace with the following:
           1G4E,B,1G67,B,POP/TZP,2004/2006,B/B,1057 1059 1061 1092 1093 1107 1108 1109 1110 1111 1112 1130 1132 1159 1152 1156 1158 1162 1186 1187 1188 1189 1206 1207 1208 1209 1210,27
         * Delete both lines for 2IYT/2IYQ and replace with the following:
           2IYT,A,2IYQ,A,ADP/SKM, 202/201,A/A,10 11 12 13 14 15 16 17 18 110 117 150 153 154 155 158 34 45 49 57 58 61 79 80 81 116 118 119 132 136,30
         * Delete all 3 lines for 1PKL/3HQP and replace with the following:
           1PKL,B,3HQP,P,ATP/FDP/OXL,1001/700/510,P/P/P,26 27 28 29 49 51 53 54 55 59 60 83 90 145 174 175 176 211 238 240 264 296 330 331 334 335 399 400 401 402 403 404 405 453 456 479 480 481 485 486 487 488 489 259 261 262 263 295,48
     There should be 93 lines in cryptic_site_locations.csv after these edits.
(12) Run match_numbering.py.  It creates the directory
     apo_holo_numbering_dicts.  The directory contains a json file for each
     apo/holo pair of proteins.  Each json file can be read into a Python
     dictionary whose keys are the residue numbers in the apo structure and
     whose values are the corresponding residues in the holo structure.  It
     only includes values for the chain used in the Cryptosite database; thus
     entries don't list the chain.

(13) Run combine_all_data.py.  It reads cryptic_site_locations.csv,
     residue_codes.json, the apo pdb files, and the json files in
     apo_holo_numbering_dicts.  It creates cryptosite_database.csv, which
     contains a line for each residue in the appropriate chain of each apo
     structure.
