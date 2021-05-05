This directory stores the code to train the ML model.  It also stores
the script that parses the jupyter notebook where the model was trained
to recreate the list of proteins used in the training database.  The
following files are noteworthy:
* train_model.ipynb: This code was used to train the model the first time.
  It assumes that the training database was set up from scratch, instead of
  being reconstructed.  (This doesn't affect which proteins are included, but
  it affects which files exist.)  Thus this code should not be run if the
  database was obtained from the reconstruction procedure.
* retrain_model.ipynb: This code retrains the model from the reconstructed
  database.  As part of this procedure, it downloads each extended-database
  protein that was used in the TACTICS database.
* get_tactics_db.py: parses train_model.ipynb to get a list of proteins
  included in the training database.
* extended_database_prots.csv: This file lists all the extended-database
  structures used in the TACTICS database.  The TACTICS database
  has a cutoff of 50 apo structures per protein; this cutoff can be seen in
  this file.  This file does not include all apo proteins in the original
  CryptoSite database; thus this file isn't a complete list of proteins used
  in the TACTICS training database.  But retrain_model.ipynb uses this file
  to get the list of proteins it needs to download.
* all_database_prots.csv: This file lists all proteins used in the TACTICS
  training database.