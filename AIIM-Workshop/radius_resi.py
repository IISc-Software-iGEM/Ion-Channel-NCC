from pymol import cmd

# Radius variable
r = 5

# Naming the selection of Na atoms
cmd.select("Na_atoms", "name Na")

# Selecting the residues with 'within' command
# The number after 'within' is the radius in Angstrom
cmd.select("radial_residues", f"chain A within {r} of Na_atoms")

# Printing the residue names & number of residues
radial_residues = []
cmd.iterate("radial_residues", "radial_residues.append((resi,resn))")
print(len(radial_residues))
radial_residues = tuple(set(radial_residues))  # otherwise each aa is counted 4 times
print(len(radial_residues))
print(radial_residues)
