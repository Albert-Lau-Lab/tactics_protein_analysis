from tactics import tactics

psf_loc = "input_data/vmd_out.psf"
dcd_loc = "input_data/vmd_out.dcd"
output_dir = "output_data/spike_test"
num_clusters = 3
tactics(output_dir, num_clusters,
        "input_data/apo_chain.pdb",
        psf_loc=psf_loc, dcd_loc=dcd_loc)

