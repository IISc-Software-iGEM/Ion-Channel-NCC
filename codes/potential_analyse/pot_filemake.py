import csv

from dx_coord import coord_to_int
from dx_elec import elec
from dx_pot_extract import extract
from dx_pot_val import val_potential

from tabulate import tabulate
import pandas as pd

def filemaker(protein, pqr_file, pot_dx_file, input_csv, destination_file):
    """
    This will make our custom potential file.
    We want the coordinate, and the potential at that coordinate.
    also each line will have x, y, z in integer.
    INFO x y z cx cy cz potential ex ey ez
    The INFO should be pqr file's data
    ATOM   N  Residue A Resi_num    x y z cx cy cz q r ex ey ez potential

    Also some pre data, which tells origin and grid length, etc.
    """
    # Read the CSV file using pandas
    csv_data = pd.read_csv(input_csv)

    # Extract metadata from the pot_dx_file
    xmin, ymin, zmin, hx, hy, hz, nx, ny, nz = extract(pot_dx_file)

    # Write metadata to the destination file
    with open(destination_file, "w") as p:
        p.write("Protein structure: " + protein + "\n")
        p.write(
            "Origin(xmin, ymin, zmin): "
            + str(xmin)
            + " "
            + str(ymin)
            + " "
            + str(zmin)
            + "\n"
        )
        p.write(
            "Grid Box Size(x y z): " + str(nx) + " " + str(ny) + " " + str(nz) + "\n"
        )
        p.write(
            "Grid length(cx cy cz): " + str(hx) + " " + str(hy) + " " + str(hz) + "\n"
        )
        p.write("Reference pqr file: " + pqr_file + "\n")
        p.write("Reference dx potential file: " + pot_dx_file + "\n\n")
        print("Written Header Files.")

    # Append the CSV data to the destination file in a clean tabular form
    table = tabulate(csv_data, headers='keys', tablefmt='plain', showindex=False)

    # Append the formatted table to the destination file
    with open(destination_file, "a") as p:
        p.write(table)
    print("Data written to CSV file.")


def csv_make(pqr_file, pot_dx_file, destination_path):
    """
    This will make the csv file containing all the info
    """
    with open(pqr_file, "r") as f:
        pqr_data = f.readlines()

    xmin, ymin, zmin, hx, hy, hz, nx, ny, nz = extract(pot_dx_file)
    with open(destination_path, "w", newline="") as p:
        writer = csv.writer(p)
        print("Written Header Files.")

        # Write column headers for the data
        writer.writerow(
            [
                "Type",
                "Num",
                "Atom",
                "Resi",
                "Chain",
                "Cx",
                "Cy",
                "Cz",
                "Q",
                "R",
                "X",
                "Y",
                "Z",
                "Ex",
                "Ey",
                "Ez",
                "Potential",
            ]
        )

        for line in pqr_data:
            line = line.split()
            cx, cy, cz, q, r = line[-5], line[-4], line[-3], line[-2], line[-1]
            x, y, z = coord_to_int(cx, cy, cz, pot_dx_file)
            ex, ey, ez = elec(x, y, z, pot_dx_file)
            potential = val_potential(cx, cy, cz, pot_dx_file)
            typ, num, atom, resi, chain = line[0], line[1], line[2], line[3], line[4]

            # Write the data row
            writer.writerow(
                [
                    typ,
                    num,
                    atom,
                    resi,
                    chain,
                    cx,
                    cy,
                    cz,
                    q,
                    r,
                    x,
                    y,
                    z,
                    ex,
                    ey,
                    ez,
                    potential,
                ]
            )


print("Starting. . .")
try:
    # csv_make(
    #    "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/7yg0.pqr",
    #    "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/7yg0_pot.dx",
    #    "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/potential.csv"
    #    )
    filemaker(
        "7yg0",
        "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/7yg0.pqr",
        "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/7yg0_pot.dx",
        "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/potential.csv",
        "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/potential_daddy.txt",
    )
    print("Your file is generated successfully.")
except Exception as e:
    print("An error occured: ", e)
    print("Process failed. Retry. . .")
