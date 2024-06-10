# Import necessary library
from potential_analyse.dx_pot_val import extract

def H_box_pdb(filepath):
    xmin, ymin, zmin, hx, hy, hz, nx, ny, nz= extract(filepath)
    gap= 20
    # Generate the coordinates for each hydrogen atom
    coordinates = [(x, y, z) for x in range(0, nx, gap) for y in range(0, ny, gap) for z in range(0, nz, gap)]
    coordinates = [(x * hx + xmin, y * hy + ymin, z * hz + zmin) for x, y, z in coordinates]
    # Function to format a coordinate line for PDB
    def format_pdb_line(atom_index, x, y, z):
        return f"HETATM{atom_index:5d}  H   UNK     1    {x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00           H\n"

    # Open a PDB file for writing
    with open("hydrogen_grid.pdb", "w") as pdb_file:
        for i, (x, y, z) in enumerate(coordinates, start=1):
            pdb_line = format_pdb_line(i, x, y, z)
            pdb_file.write(pdb_line)

    print("PDB file created successfully.")
    return