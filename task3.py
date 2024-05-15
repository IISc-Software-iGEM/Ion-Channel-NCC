'''
Code for performing task3

Selecting the residues in Chain A which are near Na Radially and save them'''
from pymol import cmd

#Load the pdb file
cmd.load(fr"c:\Users\LENOVO\Desktop\temp\gtm-475-CYS-1.pdb")

#Naming the selection of Na atoms
cmd.select("Na_atoms", "name Na")

#Selecting the residues with 'within' command
cmd.select("radial_residues", "chain A within 10 of Na_atoms")

#Save as pdb
#cmd.save(fr"C:\Users\LENOVO\Desktop\iGEM\Mutations\gtlmn-7y6i\gtm-{n}-{mutant}-{fnum}.pdb")

#Printing the residue names
radial_residues = []
cmd.iterate("radial_residues", "radial_residues.append((resi,resn))")
print(len(radial_residues))
radial_residues = tuple(set(radial_residues))
print(len(radial_residues))
print(radial_residues)
