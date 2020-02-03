load apo_conc_out_residue.pdb

bg white
set ray_shadow=0
set depth_cue=0
set ray_trace_fog=0

hide everything
remove resn hoh

select backbone, name c+n+o+ca and !het
deselect

select prot, !het
deselect

cmd.spectrum('b', 'blue_white_red', selection='prot')

color yellow, het
show sticks, het
show spheres, backbone

load apo_conc_out.dx, grid_map
isomesh grid_mesh, grid_map, 0.0
color green, grid_mesh

orient
zoom grid_mesh

#ray 1200, 1200
#png apo_conc_out.png
