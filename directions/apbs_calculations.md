# How to calculate the electrostatic potential of a protein using APBS

We have mainly three options for doing this.

1. Using the APBS web server
2. Using Pymol
3. Using Command line apbs

## Using the APBS web server

It is very straight forward. You covert pdb2pqr (automatically done) with specified parameters and then submit the job. You will get the results soon.
<br>You can download the files created for your job which may be of random names.

## Using Pymol

For Pymol you can easily visualize the electrostatic potential of a protein. Just use the APBS plugin in Pymol. When the job is done, click the `+` sign and on the map file,
go to Action -> Gradient -> Volume -> Default, this will give you the electrostatic potential field lines.
<br>
_Note:_

1. Go to the APBS configurations and set parameters. This is really important, avoid blind calculations.
2. Change the name of the temporary file created by Pymol to a more meaningful name and a better location and save it. This will give you the file which was used
   for the visualisations.

## Using Command line apbs

For Linux download the 2 Terminal toold

```bash
sudo apt-get install apbs pdb2pqr
```

This will download both of them which you can confirm using `apbs --help` or `pdb2pqr --help`.
<br>Once this is done, you can use pdb2pqr inside the terminal. Good thing, it provides lots of options to set parameters.

```bash
# Example for Usage
pdb2pqr --ff=amber --with-ph=7.0 --apbs-input protein.pdb protein.pqr # protein.pqr may not be present before
```

This will create pqr files which be uploaded in webserver or whatever you want to do with it.

<br>
For APBS, it has to be put in a file, which you make. The file should have a format(.in) where you mention the protein name and the parameters.
<br>For example, the file may look like this:

```
read mol pqr protein.pqr  # Read the protein structure
end
# Electrostatics section
elec mg-auto
dime 481 481 481  # Set grid size (e.g., 97 97 161)
cglen 481 481 481    # Define the box size (e.g., 160 160 230)
fglen 400 400 400 # Define a smaller box around the protein (e.g., 130 130 200)
mol 7yg0.pqr # which molecule this is running for. You can have many `elec` for each mol
cgcent mol 1                   # Center the grid on the molecule
fgcent mol 1                   # Center the focus box on the molecule
lpbe

bcfl sdh  # Read docs for this
# Ion definition (optional, adjust ion types and concentrations as needed)
ion 1 0.100 2.0  # 100 mM Na+ ion
ion -1 0.100 2.0 # 100 mM Cl- ion

# Define dielectric constants
pdie 4.0        # Solute dielectric
sdie 80.00      # Solvent dielectric

# Charge discretization and surface options
chgm spl0       # Linear charge discretization
srfm smol       # Smoothed molecular surface
srad 1.4        # Solvent probe radius
swin 0.3        # Spline window (not used)

# Additional options (adjust as needed)
sdens 10.0      # Sphere density
temp 298.15     # Temperature
#gamma 0.105     # Apolar coefficient

# Output options
calcenergy total   # Total- calculate energies
calcforce total    # Total- calculate forces
write qdens dx qdens # Write out charge density
write pot dx pot   # Write out electrostatic potential

end quit
```
**Note**:
1. All keywords mentioned here are required (ion is optional)
2. mg-auto -> This automatically sets up and performs a string of single-point PBE calculations to "focus" on a region of interest (binding site, etc.) in a system. It is basically an automated version of mg-manual designed for easier use.
3. 
<br>
This you write a python file which puts various file names in pdb, you have a set of parameters set for all, and then run-

```bash
apbs protein.in
```

This will give you two files called protein_qdens.dx and protein_pot.dx(or similar naming scheme may apply) which can be visualized using VMD or Pymol.
<br>See this link for a lot of tools you may need to use - https://ics.uci.edu/~dock/manuals/apbs/html/user-guide/x674.html
<br>To understand more about file structures of pqr/others, refer: https://userguide.mdanalysis.org/stable/formats/reference/pqr.html

