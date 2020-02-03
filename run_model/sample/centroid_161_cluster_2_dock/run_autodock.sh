#!/bin/bash
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/ethane_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/ethane_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/ethane_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/ethane_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/ethane_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/EOH_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/EOH_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/EOH_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/EOH_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/EOH_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/IPA_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/IPA_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/IPA_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/IPA_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/IPA_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/TBU_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/TBU_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/TBU_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/TBU_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/TBU_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/CCN_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/CCN_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/CCN_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/CCN_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/CCN_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/NME_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/NME_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/NME_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/NME_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/NME_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/DMF_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/DMF_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/DMF_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/DMF_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/DMF_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/2F2_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/2F2_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/2F2_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/2F2_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/2F2_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/HBX_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/HBX_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/HBX_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/HBX_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/HBX_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/BNZ_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/BNZ_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/BNZ_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/BNZ_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/BNZ_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/CHX_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/CHX_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/CHX_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/CHX_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/CHX_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/IPH_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/IPH_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/IPH_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/IPH_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/IPH_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/ACM_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/ACM_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/ACM_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/ACM_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/ACM_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/ACN_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/ACN_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/ACN_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/ACN_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/ACN_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/ACE_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/ACE_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/ACE_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/ACE_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/ACE_centroid_161_cluster_2.pdb -xr
vina --receptor sample/centroid_161_cluster_2_dock/centroid_161_cluster_2.pdbqt --ligand sample/centroid_161_cluster_2_dock/URE_ideal.pdbqt --center_x -19.697153 --center_y 13.487785 --center_z 112.337860 --size_x 24.689251 --size_y 20.970246 --size_z 21.916344
mv sample/centroid_161_cluster_2_dock/URE_ideal_out.pdbqt sample/centroid_161_cluster_2_dock/URE_centroid_161_cluster_2.pdbqt
obabel sample/centroid_161_cluster_2_dock/URE_centroid_161_cluster_2.pdbqt -O sample/centroid_161_cluster_2_dock/URE_centroid_161_cluster_2.pdb -xr
