#!/bin/bash
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/ethane_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/ethane_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/ethane_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/ethane_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/ethane_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/EOH_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/EOH_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/EOH_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/EOH_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/EOH_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/IPA_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/IPA_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/IPA_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/IPA_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/IPA_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/TBU_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/TBU_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/TBU_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/TBU_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/TBU_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/CCN_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/CCN_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/CCN_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/CCN_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/CCN_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/NME_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/NME_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/NME_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/NME_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/NME_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/DMF_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/DMF_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/DMF_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/DMF_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/DMF_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/2F2_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/2F2_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/2F2_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/2F2_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/2F2_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/HBX_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/HBX_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/HBX_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/HBX_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/HBX_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/BNZ_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/BNZ_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/BNZ_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/BNZ_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/BNZ_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/CHX_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/CHX_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/CHX_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/CHX_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/CHX_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/IPH_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/IPH_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/IPH_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/IPH_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/IPH_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/ACM_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/ACM_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/ACM_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/ACM_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/ACM_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/ACN_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/ACN_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/ACN_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/ACN_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/ACN_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/ACE_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/ACE_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/ACE_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/ACE_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/ACE_centroid_249_cluster_1.pdb -xr
vina --receptor sample/centroid_249_cluster_1_dock/centroid_249_cluster_1.pdbqt --ligand sample/centroid_249_cluster_1_dock/URE_ideal.pdbqt --center_x -1.093248 --center_y 30.544863 --center_z 72.989113 --size_x 38.930634 --size_y 35.101559 --size_z 39.614502
mv sample/centroid_249_cluster_1_dock/URE_ideal_out.pdbqt sample/centroid_249_cluster_1_dock/URE_centroid_249_cluster_1.pdbqt
obabel sample/centroid_249_cluster_1_dock/URE_centroid_249_cluster_1.pdbqt -O sample/centroid_249_cluster_1_dock/URE_centroid_249_cluster_1.pdb -xr
