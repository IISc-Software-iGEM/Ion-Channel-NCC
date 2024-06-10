# organisation
Input: You get a dx file, pqr and pdb file
Hopeful Output: 
1. to be able to get potential(approx) at any coordinate.
2. to get gradients around a residue or similar.

## Directions
[X] 1. Extract grid data from dx file -> xmin ymin zmin(origin), nx ny nz(grid size), hx hy hz(delta's grid length), potential data, 
FILENAME: dx_pot_extract.py

[X] 2. (optional) From hx and nx, get box length which will fit our molecule. Get H box and compare.
FILENAME: H_box_pdb.py

[X] 3. At each x y z(integer) get the potential.
FILENAME: dx_pot_int.py

[X] 4. At each x y z(integer) get cx, cy, cz(actual coordinate) and vice versa.
FILENAME: dx_coord.py

[X] 5. Get potential at cx cy cz. (Since practically we wont input x y z)
FILENAME: dx_pot_val.py

[X] 7. Create your own Potential file which has format 
```
INFO x y z cx cy cz potential
```
FILENAME: pot_filemake.py

[] 8. Gradient making
1) 