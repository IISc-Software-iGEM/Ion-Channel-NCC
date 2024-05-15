# This file is to be run in pymol, first fetch the either 7yg0/7y6i then use `run mutation_2.py` after directing into the directory where it is saved.
# This file lets you save all the rotamers in a mutation given the residue number and mutant 


from pymol import cmd

# Open the file and read the lines
with open('mutations.txt', 'r') as f:
    lines = f.readlines()

#This is the raw code from mutation.py which i modified for this file
def everything():
    # Loop over the lines
    for line in lines:
        # Split the line into residue number (n) and mutant
        n, mutant = line.strip().split()

        # Use the values in your code
        cmd.wizard("mutagenesis")
        cmd.get_wizard().set_mode(mutant)
        cmd.get_wizard().do_select(f"chain A and resid {n}")
        # To get minimum strain, comment the next line. Else, you ll get max %
        cmd.frame(1)
        cmd.get_wizard().apply()
        # Close wiard
        cmd.wizard(None)

        #cmd.save(f"/Volumes/Anirudh/IISc/IGEM/gtlmn-7yg0/gtm-{n}-{mutant}.pdb")
        cmd.save(fr"C:\Users\LENOVO\Downloads\gtm-{n}-{mutant}.pdb")

#This function contains the actual code for this file
def perMutant(num):
    # Loop over the lines
    for line in lines:
        n, mutant = line.strip().split()
        if num == int(n):
             # Use the values in your code
            cmd.wizard("mutagenesis")
            cmd.get_wizard().set_mode(mutant)
            cmd.get_wizard().do_select(f"chain A and resid {n}")
            # To get alll the rotamers...
            totfnum = cmd.count_frames() 
            for fnum in range(1, totfnum + 1):
                cmd.frame(fnum)
                cmd.save(fr"C:\Users\LENOVO\Desktop\iGEM\Mutations\gtlmn-7y6i\gtm-{n}-{mutant}-{fnum}.pdb")
            
            # Close wiard
            cmd.wizard(None)
            

            #cmd.save(f"/Volumes/Anirudh/IISc/IGEM/gtlmn-7yg0/gtm-{n}-{mutant}.pdb")

#change the residue number here          
perMutant(475)
