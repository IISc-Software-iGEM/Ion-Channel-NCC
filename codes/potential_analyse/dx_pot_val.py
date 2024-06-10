from dx_pot_extract import extract
from dx_coord import coord_to_int

def val_potential(cx, cy, cz, filepath):
    """
    This file will extract the potential value at cx, cy, cz.
    The convert it to x,y,z and extract the potential value.
    """

    xmin, ymin, zmin, hx, hy, hz, nx, ny, nz, data = extract(filepath, return_data=True)
    x,y,z = coord_to_int(cx, cy, cz, filepath)
    # Extract the potential data
    # Formula for which line to target 
    total_z = x * ny * nz + y * nz + z
    # # Calculate the line number and the position within the line
    line_number = total_z // 3 
    position = total_z % 3
    # Extract the potential from the data
    potential = data[line_number].split()[position]

    return potential
