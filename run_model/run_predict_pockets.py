from predict_pockets import predict_pockets

psf_loc = "../glua2-w.psf"
dcd_loc = "../traj_18_23.dcd"
#dcd_loc = "../glua2-w.000000.dcd"
#output_dir = "delete_me"
#run_name = "delete_me"
#num_clusters = 2
output_dir = "cluster_output_18_23_with_9_clusters_mindist_11"
num_clusters = 9
run_name = "traj_18_23_with_9_clusters_mindist_11"
predict_pockets(psf_loc, dcd_loc, output_dir, num_clusters, run_name,
                "frame_0_with_chain.pdb")
