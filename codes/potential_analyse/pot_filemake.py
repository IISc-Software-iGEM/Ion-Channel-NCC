from dx_pot_extract import extract
from dx_pot_val import val_potential
from dx_coord import coord_to_int
from dx_elec import elec

def filemaker(protein, pqr_file, pot_dx_file):
    """
    This will make our custom potential file.
    We want the coordinate, and the potential at that coordinate. 
    also each line will have x, y, z in integer.
    INFO x y z cx cy cz potential ex ey ez
    The INFO should be pqr file's data
    ATOM   N  Residue A Resi_num    x y z cx cy cz q r potential ex ey ez

    Also some pre data, which tells origin and grid length, etc.
    """
    with open(pqr_file, "r") as f:
        pqr_data= f.readlines()

    xmin, ymin, zmin, hx, hy, hz, nx, ny, nz= extract(pot_dx_file)
    with open("/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/potential.txt", "w") as p:
        p.write("Protein structure: " + protein + "\n")
        p.write("Origin(xmin, ymin, zmin): " + str(xmin) + " " + str(ymin) + " " + str(zmin) + "\n")   
        p.write("Grid Box Size(x y z): " + str(nx) + " " + str(ny) + " " + str(nz) + "\n")
        p.write("Grid length(cx cy cz): " + str(hx) + " " + str(hy) + " " + str(hz) + "\n")
        p.write("Reference pqr file: " + pqr_file + "\n")
        p.write("Reference dx potential file: " + pot_dx_file + "\n\n")
        print("Written Header Files.")

        for line in pqr_data:
            line = line.split()
            cx, cy, cz, q, r = line[-5], line[-4], line[-3], line[-2], line[-1]
            x,y,z = coord_to_int(cx, cy, cz, pot_dx_file)
            potential = val_potential(cx, cy, cz, pot_dx_file)
            ex, ey, ez = elec(x, y, z, pot_dx_file)
            p.write("{:<10} {:<6} {:<6} {:<6} {:<6} {:<10} {:<10} {:<10} {:<10} {:<10} {:<25} {:<25} {:<25}\n".format(
                '    '.join(line[:-5]), str(x), str(y), str(z), str(cx), str(cy), str(cz), str(q), str(r), str(potential), str(ex), str(ey), str(ez)))
    return
print("Starting. . .")
filemaker("7yg0", "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/7yg0.pqr", "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/7yg0_pot.dx")
print("Your file is generated successfully.")