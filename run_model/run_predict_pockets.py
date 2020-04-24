from predict_pockets import predict_pockets

psf_loc = "input_data/vmd_out.psf"
dcd_loc = "input_data/vmd_out.dcd"
output_dir = "output_data/spike_test"
num_clusters = 3
run_name = "spike_test"
predict_pockets(output_dir, num_clusters, run_name,
                "input_data/apo_chain.pdb",
                psf_loc=psf_loc, dcd_loc=dcd_loc)

