
'''
STEPS:
After making the necessary changes to this file
1) Open Chimera, open command line
2) type: cd C:\Users\LENOVO\Code\forks\Ion-Channel-NCC\codes
3) type: open add_H2.py 
'''

import chimera
from chimera import runCommand as rc
from chimera import openModels, Molecule

# This script adds hydrogens to a loaded PDB file in UCSF Chimera
def add_hydrogens(pdb_path):
    # Load the PDB file
    rc("open " + pdb_path)

    # Add hydrogens
    rc("addh")

    # Save the modified PDB file with hydrogens in the same folder
    new_pdb_path = pdb_path.replace('.pdb', '_withH.pdb')
    rc("write format pdb 0 " + new_pdb_path)
    rc("close all")
    print("Hydrogens added and saved to", new_pdb_path)

# Example usage:
# Replace 'path_to_your_pdb.pdb' with the path to your PDB file.
#add_hydrogens(path_to_your_pdb.pdb)

#Now, for the magic
def add_hydrogens_multiple(protein, n, mutant):
    for state in range(1, 31):
        pdb_path = "C:\\Users\\LENOVO\\Code\\forks\\Ion-Channel-NCC\\mutation_morphs\\{protein}\\gtm-{n}-{mutant}\\gtm-{n}-{mutant}-{state}.pdb".format(protein = protein, n = n, mutant = mutant, state = state )
        add_hydrogens(pdb_path)
        

add_hydrogens_multiple('7y6i', 475, 'CYS')