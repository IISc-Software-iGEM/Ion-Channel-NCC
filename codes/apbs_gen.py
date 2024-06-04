import subprocess
import os

def pdb2pqr(proteins:list):
    """
    We run pdb2pqr to convert pdb file to pqr file. The main command that we will be running is - 
    pdb2pqr --ff=AMBER --apbs-input=protein.in --keep-chain --whitespace --drop-water --titration-state-method=propka --with-ph=7 protein.pdb protein.pqr

    More options can be changed here, like force field(Amber currently).
    Compulsary options are - 
    1. --apbs-input=protein.in
    2. --keep-chain
    3. --whitespace

    This function will also be interactive, where user can select the options they want to change.
    """
    main_command= "pdb2pqr --ff=AMBER --keep-chain --whitespace --drop-water --titration-state-method=propka --with-ph=7"
    verify_txt = f"The below options will be used by default: \n{main_command}. \nDo you want to change any options? (y/n)"
    cont = input(verify_txt)
    if cont.lower() == 'n' or cont.lower() == 'no':
        new_command = input("Please enter new commands to run(write the whole thing: )")
        main_command = new_command
    print("Running pdb2pqr command seqeuentially for all proteins...")

    for protein in proteins:
        try:
            subprocess.run(f"{main_command} --apbs-input={protein}.in {protein}.pdb {protein}.pqr", shell=True)
            print(f"pdb2pqr command ran successfully for {protein}. Files generated: {protein}.pqr, {protein}.in")
        except:
            print(f"Error in running pdb2pqr command for {protein}. Return None")
    return

def input_changes(proteins:list):
    """
    This will change the input file of the protein.in file, with the manually set conditions.
    1) Change the dielectric values
       Here change pdie from 2.0000 to 4.0000 and sdie from 78.5400 to 80.0000

    2) Add the write command
        calcenergy comps
        write pot dx {protein}_pot.dx
    """
    try:
        for protein in proteins:
            print(f"Changing the input file of the {protein}.in file.")
            with open(f"{protein}.in", "r") as f:
                lines = f.readlines()
            with open(f"{protein}.in", "w") as f:
                for line in lines:
                    if "pdie" in line:
                        f.write("    pdie 4.0000\n")
                    elif "sdie" in line:
                        f.write("    sdie 80.0000\n")
                    elif "calcenergy" in line:
                        f.write(f"    calcenergy comps\nwrite pot dx {protein}_pot.dx")
                    else:
                        f.write(line)
    except:
        print(f"Error in changing the input file for {protein}. Could not change.")
    return

def apbs(proteins:list):
    """
    This will run the apbs command for the protein.in file.
    The command which will run is - `apbs protein.in`
    """
    main_command = "apbs"
    options=""
    options_add = input("Do you want to add any options for apbs command? (y/n)")
    if options_add.lower() == 'y' or options_add.lower() == 'yes':
        options = input("Please enter the new command: ")
    print("Running apbs command seqeuentially for all proteins...")
    for protein in proteins:
        input_changes(proteins)
        try:
            subprocess.run(f"{main_command} {options} {protein}.in", shell=True)
            print(f"apbs command ran successfully for {protein}.")
        except:
            print(f"Error in running apbs command for {protein}. Return None")
    return

def main():
    """
    The main function is a cumulative function that will run all the above functions in a sequence.

    Methodology (steps): 
    1. Run pdb2pqr command - This will generate protein.pqr file and protein.in file.
    2. Make changes to protein.in file, if required. (like write command, etc. dielectric values)
    3. Run protein.in file, using `apbs protein.in`- This will create the output potential (+other if required) files.
    4. Analyse the potential files
    """
    # The directory where this command will run will have all the protein.pdb files. Extract protein name
    proteins = [i.split(".")[0] for i in os.listdir() if i.endswith(".pdb")]
    print(f"Proteins found in the directory: {proteins}")
    print(f"Let's start the procedure for APBS calculations for the proteins(in pdb files).")
    start = input("Do you want to run pdb2pqr command? (y/n)")
    if start.lower() == 'y' or start.lower() == 'yes':
        pdb2pqr(proteins)
    else:
        print("Without the above Exiting the program.")
        return
    start = input("Do you want to run apbs command? (y/n)")
    if start.lower() == 'y' or start.lower() == 'yes':
        apbs(proteins)
    else:
        print("Without the above Exiting the program.")
        return
    print("The APBS calculations are done.")
    return