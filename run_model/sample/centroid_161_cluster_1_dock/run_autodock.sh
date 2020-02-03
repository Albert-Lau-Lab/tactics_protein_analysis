#!/bin/bash
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/ethane_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/ethane_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/ethane_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/ethane_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/ethane_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/EOH_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/EOH_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/EOH_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/EOH_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/EOH_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/IPA_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/IPA_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/IPA_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/IPA_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/IPA_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/TBU_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/TBU_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/TBU_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/TBU_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/TBU_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/CCN_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/CCN_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/CCN_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/CCN_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/CCN_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/NME_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/NME_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/NME_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/NME_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/NME_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/DMF_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/DMF_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/DMF_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/DMF_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/DMF_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/2F2_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/2F2_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/2F2_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/2F2_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/2F2_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/HBX_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/HBX_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/HBX_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/HBX_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/HBX_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/BNZ_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/BNZ_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/BNZ_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/BNZ_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/BNZ_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/CHX_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/CHX_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/CHX_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/CHX_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/CHX_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/IPH_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/IPH_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/IPH_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/IPH_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/IPH_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/ACM_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/ACM_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/ACM_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/ACM_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/ACM_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/ACN_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/ACN_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/ACN_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/ACN_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/ACN_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/ACE_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/ACE_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/ACE_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/ACE_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/ACE_centroid_161_cluster_1.pdb -xr
vina --receptor sample/centroid_161_cluster_1_dock/centroid_161_cluster_1.pdbqt --ligand sample/centroid_161_cluster_1_dock/URE_ideal.pdbqt --center_x -44.714897 --center_y 11.421534 --center_z 100.848160 --size_x 21.435406 --size_y 24.688217 --size_z 23.354149
mv sample/centroid_161_cluster_1_dock/URE_ideal_out.pdbqt sample/centroid_161_cluster_1_dock/URE_centroid_161_cluster_1.pdbqt
obabel sample/centroid_161_cluster_1_dock/URE_centroid_161_cluster_1.pdbqt -O sample/centroid_161_cluster_1_dock/URE_centroid_161_cluster_1.pdb -xr
