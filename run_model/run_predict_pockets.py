from predict_pockets import predict_pockets

psf_loc = "input_data/data-7/glua2-w.psf"
dcd_loc = "input_data/data-7/data7_traj_0_5.dcd"
output_dir = "output_data/data7_traj_0_5"
num_clusters = 9
run_name = "data7_traj_0_5"
predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name,
                "input_data/data-7/frame_0_with_chain.pdb")
