from predict_pockets import predict_pockets

psf_loc = "input_data/data-5/glua2-w.psf"
dcd_loc = "input_data/data-5/data5_traj_0_5.dcd"
output_dir = "output_data/data5_traj_0_5"
num_clusters = 9
run_name = "data5_traj_0_5"
predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name,
                "input_data/data-5/data5_frame0_with_chain.pdb")
