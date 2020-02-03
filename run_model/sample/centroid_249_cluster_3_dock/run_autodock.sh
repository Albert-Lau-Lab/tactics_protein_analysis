#!/bin/bash
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/ethane_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/ethane_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/ethane_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/ethane_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/ethane_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/EOH_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/EOH_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/EOH_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/EOH_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/EOH_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/IPA_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/IPA_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/IPA_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/IPA_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/IPA_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/TBU_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/TBU_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/TBU_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/TBU_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/TBU_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/CCN_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/CCN_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/CCN_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/CCN_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/CCN_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/NME_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/NME_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/NME_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/NME_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/NME_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/DMF_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/DMF_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/DMF_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/DMF_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/DMF_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/2F2_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/2F2_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/2F2_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/2F2_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/2F2_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/HBX_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/HBX_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/HBX_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/HBX_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/HBX_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/BNZ_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/BNZ_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/BNZ_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/BNZ_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/BNZ_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/CHX_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/CHX_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/CHX_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/CHX_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/CHX_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/IPH_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/IPH_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/IPH_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/IPH_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/IPH_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/ACM_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/ACM_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/ACM_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/ACM_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/ACM_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/ACN_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/ACN_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/ACN_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/ACN_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/ACN_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/ACE_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/ACE_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/ACE_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/ACE_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/ACE_centroid_249_cluster_3.pdb -xr
vina --receptor sample/centroid_249_cluster_3_dock/centroid_249_cluster_3.pdbqt --ligand sample/centroid_249_cluster_3_dock/URE_ideal.pdbqt --center_x -11.648589 --center_y 17.173769 --center_z 32.368111 --size_x 32.421103 --size_y 26.561123 --size_z 28.564816
mv sample/centroid_249_cluster_3_dock/URE_ideal_out.pdbqt sample/centroid_249_cluster_3_dock/URE_centroid_249_cluster_3.pdbqt
obabel sample/centroid_249_cluster_3_dock/URE_centroid_249_cluster_3.pdbqt -O sample/centroid_249_cluster_3_dock/URE_centroid_249_cluster_3.pdb -xr
