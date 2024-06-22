def file_xyz(protein:str):
    """
    This file creates the .xyz format for our protein. This will take the data from the master file.
    XYZ file format-

    Number of atoms
    Comment line(inclue protein.pdb and origin coordinates)
    Atom1 x y z
    . . .
    """
    with open(f"/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/potential.txt", "r") as m:
        master_data= m.readlines()

    origin, num_atoms, i = "", 0, 0
    with open(f"./potential_analyse/formatted_files/{protein}.xyz", "w") as f:
        for j, line in enumerate(master_data):
            if "ATOM" in line or "HETATM" in line:
                num_atoms = len(master_data) - j
                i = j
                break
            if "Origin" in line:
                origin = line.split(":")[1].split(" ")
                print(origin)
                xmin, ymin, zmin = origin[1], origin[2], (origin[3][:-2] if "\n" in origin[3] else origin[3])

        f.write(str(num_atoms) + "\n")
        f.write(f"Protein: {protein}.pdb Origin: {xmin} {ymin} {zmin}\n")

        for line in master_data[i:]:
            line = line.split()
            atom= line[2]
            f.write(f"{atom}") # Atom name
            f.write(" "*(len(str(num_atoms))+1-len(atom))+ f"{line[9]}    {line[10]}  {line[11]}\n")
