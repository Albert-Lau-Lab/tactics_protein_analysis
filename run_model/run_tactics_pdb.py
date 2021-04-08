from tactics import tactics
import MDAnalysis


universe = MDAnalysis.Universe("/home/devans61/Desktop/covid-19/capstics/protease_dimer_structures/6M03_segid.pdb",
                               "/home/devans61/Desktop/covid-19/capstics/protease_dimer_structures/6Y2E_segid.pdb",
                               "/home/devans61/Desktop/covid-19/capstics/protease_dimer_structures/6Y2G_segid.pdb",
                               "/home/devans61/Desktop/covid-19/capstics/protease_dimer_structures/5R7Y_segid.pdb",
                               "/home/devans61/Desktop/covid-19/capstics/protease_dimer_structures/5R7Z_segid.pdb",
                               "/home/devans61/Desktop/covid-19/capstics/protease_dimer_structures/5R80_segid.pdb",
                               "/home/devans61/Desktop/covid-19/capstics/protease_dimer_structures/5R81_segid.pdb",
                               "/home/devans61/Desktop/covid-19/capstics/protease_dimer_structures/5R82_segid.pdb")


output_dir = "output_data/protease"
num_clusters = 7
run_name = "protease"
tactics(output_dir, num_clusters, run_name,
        "/home/devans61/Desktop/covid-19/tactics/protease_dimer_structures/6M03_aligned.pdb",
        universe=universe,  ml_score_thresh=0.3, ml_std_thresh=0.1)

