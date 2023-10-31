# TACTICS Pocket Finder Code
This code finds the locations of possible cryptic pockets within MD trajectories.

## Installing TACTICS
One of TACTICS's dependencies cannot be installed on Mac OS &#8805; Catalina.  (See [here](https://ccsb.scripps.edu/mgltools/) for details.)  Therefore we recommend installing TACTICS on Linux.

TACTICS is strict about which versions of Python packages are used.  We recommend installing in a Python virtual environment so the rest of the computer is unaffected.

### Standard Installation Instructions

Install pyenv using [these instructions](https://brain2life.hashnode.dev/how-to-install-pyenv-python-version-manager-on-ubuntu-2004).

Download TACTICS with the command`git clone https://github.com/Albert-Lau-Lab/tactics_protein_analysis.git`.  Use `cd` to enter the directory `tactics_protein_analysis`.  Within this directory, run the following commands:

    pyenv install 3.8.16
    pyenv local 3.8.16
    
Check that when you type the command `python` within the TACTICS directory, you get version 3.8.16.  (You should still get the default Python when outside the TACTICS directory.)

**While in the TACTICS directory,** run the following:
    
    sudo apt-get install openbabel
    sudo apt-get install autodock-vina
    sudo apt-get install concavity
    sudo apt-get install pymol
    
    pip install cython
    pip install numpy==1.19.5
    pip install scikit-learn==0.21.2
    pip install mdanalysis==2.2.0
    pip install pandas==1.4.4
    
Download the latest version of MGLTools from [here](https://ccsb.scripps.edu/mgltools/downloads/).  After downloading MGLTools, run `./install.sh` to install it.  See MGLTools README for more info.

Install VMD so it can be run using by typing `vmd` into the terminal.
    
Modify the TACTICS file `get_dock_score.py` so that `mgltools_loc`, `pythonsh_loc`, and `prepare_receptor_loc` store the locations of the MGLTools software.


### Alternative Installation Using Docker
See the appendix [here](#appendix).


## Usage
#### Location of the Code

Users should run TACTICS while `run_model` is the working directory.

#### How to Run the Code

**Warning: the MD trajectory should be aligned to itself, so that the center of mass remains constant.  This matters because TACTICS finds the change in residue positions; motion of the entire protein would bias this.**

TACTICS is run by calling a Python function.  Running TACTICS will usually require the following:

* `output_dir`: the name of the directory where the output will be stored.
* `apo_pdb_loc`: the location of the "apo" structure before MD has started. This is compared with the frames from the MD trajectory.
* `universe` : an MDAnalysis Universe object containing the MD data.  See the example below for how to create this.
* `num_clusters`: how many frames of the MD trajectory should be selected by TACTICS for analysis.  We recommend starting with 8 and trying a few values until you get reasonable-looking results.  Values of roughly 3-15 are reasonable.
* `ml_score_thresh`: the ML confidence score threshold for determining if a residue is "high-scoring".  The default value is 0.8.  You might need to try a few values to get reasonable output.  Values between 0.5 and 0.9 should work for most systems, but anything between 0 and 1 is allowed.
* `ml_std_thresh`: the algorithm ignores residues that have high ML confidence scores in all frames.  It does this by ignoring residues for which the standard deviation of the confidence scores among MD snapshots is less than `ml_std_thresh`.  The default value is 0.25.  Values between 0.05 and 0.4 are suggested, but anything between 0 and 1 is allowed.
            
##### Example Usage
    import MDAnalysis as mda
    from tactics import tactics
    
    output_dir = "test_output"
    apo_pdb_loc = "/data/sample_first_frame.pdb"
    psf_loc = "/data/sample.psf"
    dcd_locs = ["/data/sample1.dcd", "/data/sample2.dcd"]
    u = mda.Universe(psf_loc, dcd_list)
    
    tactics(output_dir, apo_pdb_loc, universe=u, num_clusters=8,
            ml_score_thresh=0.8, ml_std_thresh=0.25)
    
Additional options are discussed in the [appendix](#appendix). 
 
#### What Files Are Created?
 
 
 `output_dir` contains many files.  Most of them are created by intermediate steps of the algorithm and aren't useful.  Here are the files that are expected to be useful:
 
  * `display_black_bg.pml` is a PyMOL script to display the results.  Recall that the function `tactics` begins by clustering the MD trajectory based on structure.  This PyMOL script displays a frame from each cluster; it does the following:
    * Residues that are predicted by ML to be in cryptic pockets are shown in white sticks.
    * Residues with high ML scores are clustered; fragment docking is done on each cluster.  The B-factor putty displays the fragment dock scores.
    * The boxes show the boundaries for the fragment dock calculations.  They are slightly larger than the predicted binding sites.
  * `display_white_bg.pml` is similar to `display_black_bg.pml`, except that the ML predictions are shown in black and the background is white.  The white background is often more suitable for making publication images than the black background.
  * Each cluster's structure is written to the file `centroid_<cluster_num>.pdb` where `<cluster_num>` is the number of the cluster.
  * `written_output.txt` lists each predicted site.  It records the center and size of each docking box (from when Autodock Vina was run within the algorithm); this can be used as an approximate quantification of the site's location.
  * `times.txt` lists the total time in seconds that TACTICS took to run, along with the times taken by several steps of the algorithm.
#### How Can the Output Be Interpreted?
First, change the working directory to whatever was passed as `output_dir`.  Then, run one of the PyMOL scripts.  The script displays all clusters.  This is necessary in order to get PyMOL to scale the b-factors correctly.  But it's hard to understand.  To examine the output, do the following:

 * Hide everything.
 * Display a single cluster, and the boxes for it.
 * Examine the box size.  If the box is too big, then the fragment docking will be inaccurate.  If the box is no bigger than a typical protein domain, then the docking should work.
     * If a box is too big, this means that the algorithm can't work on that part of the structure.  Ignore that area; hopefully the issue isn't present in all snapshots.
     * Occasionally, a small box will be partially or entirely within a larger box.  The overlap may impact the reliability of the dock scores; this should be considered when interpreting the code's output in this situation.
 * Examine the sticks (ML predictions) and b-factor putty (fragment docking).  Ideally, the residues with sticks should also have high b-factors.  This means that the ML prediction and docking agree.
     * If the sticks and the high b-factors are in different areas, then fragment docking didn't support the ML prediction.  This means the prediction is probably incorrect; there is probably no pocket.
 * It may be useful to load `centroid_<cluster_num>.pdb` and display it as a cartoon.  This will make it easier to determine where in the protein each predicted pocket is.
 * Repeat the process for each cluster centroid.

## Debugging
If the computer runs out of RAM, it may stop running the code and give the error message `Killed`.  If this happens, reduce the size of the input file or free up more RAM.

If the code predicts numerous pockets but each pocket only has one residue, then the segids of the input may be wrong.  They must be of the form `PROA`, `PROB`, etc.

If the code predicts no pockets, then `ml_score_thresh` and `ml_std_thresh` may be too high.

If the code gives the error message `KeyError: '1:A'`, then the apo structure's residue and chain nomenclature may not match the nomenclature used in the trajectory.

## <a name="appendix"></a> Appendix
### Alternative Installation Using Docker
* Install Docker.  On Ubuntu, `apt-get` is an easy way to get Docker: `sudo apt-get install Docker`.
* Clone the TACTICS GitHub repository: ` git clone https://github.com/Albert-Lau-Lab/tactics_protein_analysis.git`
* Download a tar.gz file of VMD.  The file will probably be named something like `vmd-1.9.3.bin.LINUXAMD64.text.tar.gz`.  Copy the VMD file into the `tactics_protein_analysis` directory that you cloned from GitHub.
* `cd` into `tactics_protein_analysis`.  Run the following command: `sudo docker build --no-cache .`.  It might take several minutes to run.
* Run the following command: `sudo docker images`.  You should see a Docker image listed whose `REPOSITORY` is `<none>` and `SIZE` is approximately 2.4GB.  Copy the image's `IMAGE ID`.
* Paste the `IMAGE ID` into this command: ` sudo docker run -v $(pwd):/tactics_docker_dir/tactics_protein_analysis -it <IMAGE_ID>`.  For example: ` sudo docker run -v $(pwd):/tactics_docker_dir/tactics_protein_analysis -it ef423c81aa8f`
* You will now be inside the Docker container.  It functions similarly to a virtual machine.  The container's filesystem is different from the host computer's filesystem; files created by the container aren't visible from the rest of the host computer (and vice versa).  The exception to this is that the container and the host share the `tactics_protein_analysis` directory.  Anything inside this directory can be edited by both the container and the host machine.
* Run TACTICS while inside the container.  NOTE: your input MD data must be inside `tactics_protein_analysis` in order to be seen by the container.  The recommended location is `tactics_protein_analysis/run_model/input_data`.
* To exit the container, press Control D or type `exit`.
* To restart the container: first type `sudo docker container ls -a` to list the containers.  Copy the container ID (not the image ID).  Then type `sudo docker start -i <container id>` where `<container_id>` is replaced with the correct value.
* WARNING: Creating many Docker images/containers can quickly use up memory.  To delete them:
    * `sudo docker container ls -a` to get the container IDs.
    * `sudo docker rm <container id>` to delete the containers.
    * `sudo docker images` to get the image IDs.
    * `sudo docker rmi <image id>` to delete the images.

### Additional Options For TACTICS
Here is a full list of possible arguments to TACTICS:

```
tactics(output_dir, apo_pdb_loc, psf_loc=None, dcd_loc=None, universe=None,
        num_clusters=None, alt_clustering_method=None, ml_score_thresh=0.8,
        ml_std_thresh=0.25, dock_extra_space=8, clust_max_dist=11)
```
Here is an explanation of the arguments not discussed above:

 * `psf_loc` and `dcd_loc` : string, optional.  Instead of passing an MDAnalysis Universe, users can pass the locations of a psf and a dcd file.  To do this, both `psf_loc` and `dcd_loc` must be given and `universe` must be `None`.
 * `alt_clustering_method` : MDAnalysis ClusteringMethod object.  An algorithm used to be used to cluster the trajectory.  If `alt_clustering_method` is `None`, then k-means will be used.  Either `alt_clustering_method` or `num_clusters` must be `None`.
 * `dock_extra_space` : float, optional.  The space (in Angstroms) added to each side of the predicted site when determining the region to perform docking in.  The default value is 8.  This value is not expected to need changing from system to system; the default value is recommended.
 * `clust_max_dist` : float, optional.  The distance threshold (in Angstroms) to determine if a residue with a high ML score should be included in a cluster of other high-scoring residues.  The default value is 11.  This value is not expected to need changing from system to system; the default value is recommended.

##### Example Using PSF/DCD Instead of Universe
    from tactics import tactics
    
    output_dir = "test_output"
    apo_pdb_loc = "/data/sample_first_frame.pdb"
    psf_loc = "/data/sample.psf"
    dcd_loc = "/data/sample.dcd"
    
    tactics(output_dir, apo_pdb_loc, psf_loc=psf_loc, dcd_loc=dcd_loc,
            num_clusters=8, ml_score_thresh=0.8, ml_std_thresh=0.25)
