# This file is to be run in pymol, using `run mutation.py` after directing into the directory where it is saved.
# This file contains methods on how to mutate the files with the best rotamer, which is frame 1 by default. 
# We have to select frame 1 since it's not chosen by default. You can run these commands by hand in pymol too.

from pymol import cmd

# Open the file and read the lines
with open('mutations.txt', 'r') as f:
    lines = f.readlines()

# Loop over the lines
for line in lines:
    # Split the line into residue number (n) and mutant
    n, mutant = line.strip().split()

    # Use the values in your code
    cmd.wizard("mutagenesis")
    cmd.get_wizard().set_mode(mutant)
    cmd.get_wizard().do_select(f"chain A and resid {n}")
    # To get minimum strain, comment the next line. Else, you ll get max %
    cmd.frame(1)
    cmd.get_wizard().apply()
    # Close wiard
    cmd.wizard(None)

    cmd.save(f"/Volumes/Anirudh/IISc/IGEM/gtlmn-7yg0/gtm-{n}-{mutant}.pdb")
