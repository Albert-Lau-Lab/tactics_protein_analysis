#!/bin/bash
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/ethane_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/ethane_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/ethane_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/ethane_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/ethane_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/EOH_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/EOH_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/EOH_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/EOH_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/EOH_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/IPA_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/IPA_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/IPA_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/IPA_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/IPA_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/TBU_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/TBU_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/TBU_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/TBU_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/TBU_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/CCN_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/CCN_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/CCN_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/CCN_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/CCN_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/NME_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/NME_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/NME_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/NME_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/NME_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/DMF_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/DMF_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/DMF_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/DMF_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/DMF_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/2F2_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/2F2_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/2F2_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/2F2_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/2F2_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/HBX_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/HBX_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/HBX_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/HBX_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/HBX_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/BNZ_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/BNZ_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/BNZ_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/BNZ_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/BNZ_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/CHX_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/CHX_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/CHX_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/CHX_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/CHX_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/IPH_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/IPH_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/IPH_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/IPH_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/IPH_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/ACM_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/ACM_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/ACM_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/ACM_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/ACM_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/ACN_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/ACN_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/ACN_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/ACN_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/ACN_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/ACE_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/ACE_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/ACE_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/ACE_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/ACE_centroid_161_cluster_0.pdb -xr
vina --receptor sample/centroid_161_cluster_0_dock/centroid_161_cluster_0.pdbqt --ligand sample/centroid_161_cluster_0_dock/URE_ideal.pdbqt --center_x 5.318464 --center_y 31.059025 --center_z 66.176239 --size_x 36.694027 --size_y 39.173101 --size_z 54.456413
mv sample/centroid_161_cluster_0_dock/URE_ideal_out.pdbqt sample/centroid_161_cluster_0_dock/URE_centroid_161_cluster_0.pdbqt
obabel sample/centroid_161_cluster_0_dock/URE_centroid_161_cluster_0.pdbqt -O sample/centroid_161_cluster_0_dock/URE_centroid_161_cluster_0.pdb -xr
