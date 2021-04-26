from tactics import tactics

psf_loc = "input_data/vmd_out.psf"
dcd_loc = "input_data/vmd_out.dcd"
output_dir = "output_data/spike_test"
alt_clustering_method = clustering.ClusteringMethod.AffinityPropagation()
tactics(output_dir,
        "input_data/apo_chain.pdb",
        psf_loc=psf_loc, dcd_loc=dcd_loc, alt_clustering_method=alt_clustering_method)

