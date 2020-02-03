from predict_pockets import predict_pockets

psf_loc = "input_data/glua2-w.psf"
dcd_loc = "input_data/glua2-w.000000.dcd"
output_dir = "output_data/sample"
num_clusters = 3
run_name = "sample"
predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name,
                "input_data/frame_0_with_chain.pdb")
