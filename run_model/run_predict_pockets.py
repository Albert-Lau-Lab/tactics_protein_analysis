from predict_pockets import predict_pockets

psf_loc = "input_data/data-5/glua2-w.psf"
dcd_loc = "input_data/data-5/data5_traj_0_5.dcd"
output_dir = "output_data/data5_traj_0_5"
num_clusters = 9
run_name = "data5_traj_0_5"
predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name,
                "input_data/data-5/data5_frame0_with_chain.pdb")

psf_loc = "input_data/data-5/glua2-w.psf"
dcd_loc = "input_data/data-5/data5_traj_6_11.dcd"
output_dir = "output_data/data5_traj_6_11"
num_clusters = 9
run_name = "data5_traj_6_11"
predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name,
                "input_data/data-5/data5_frame0_with_chain.pdb")

psf_loc = "input_data/data-5/glua2-w.psf"
dcd_loc = "input_data/data-5/data5_traj_12_17.dcd"
output_dir = "output_data/data5_traj_12_17"
num_clusters = 9
run_name = "data5_traj_12_17"
predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name,
                "input_data/data-5/data5_frame0_with_chain.pdb")

psf_loc = "input_data/data-5/glua2-w.psf"
dcd_loc = "input_data/data-5/data5_traj_18_23.dcd"
output_dir = "output_data/data5_traj_18_23"
num_clusters = 9
run_name = "data5_traj_18_23"
predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name,
                "input_data/data-5/data5_frame0_with_chain.pdb")

psf_loc = "input_data/data-5/glua2-w.psf"
dcd_loc = "input_data/data-5/data5_traj_24_29.dcd"
output_dir = "output_data/data5_traj_24_29"
num_clusters = 9
run_name = "data5_traj_24_29"
predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name,
                "input_data/data-5/data5_frame0_with_chain.pdb")

psf_loc = "input_data/data-5/glua2-w.psf"
dcd_loc = "input_data/data-5/data5_traj_30_35.dcd"
output_dir = "output_data/data5_traj_30_35"
num_clusters = 9
run_name = "data5_traj_30_35"
predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name,
                "input_data/data-5/data5_frame0_with_chain.pdb")
