Most users of the software will NOT need to run code in this directory.  This
code is used to generate the training database and train the model.  Because
the git repository includes the trained model, re-training the model isn't
necessary in order to run TACTICS.  Nevertheless, this code is included for reference.

Originally, the training database was generated in the directoy generate_training_database.
This database was used to train the ML model in the directory ml.  The code in
generate_training_database was executed before the code in ml.

Later, the training database was reconstructed.  The list of proteins was taken from
the jupyter notebook that trained the ML model.  The proteins in the extended database
were downloaded using a script in the generate_training_database/ext_crypto_database
directory; the proteins in the original CryptoSite database were downloaded in
generate_training_database/gen_crypto_database.
