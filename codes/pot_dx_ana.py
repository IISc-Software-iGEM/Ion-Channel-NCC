def dx_pot_analyser(x,y,z,filepath):
    """
# Data from APBS 3.4.1
#
# POTENTIAL (kT/e)
#
object 1 class gridpositions counts 353 193 257
origin 6.617750e+01 9.325490e+01 7.383950e+01
delta 4.895710e-01 0.000000e+00 0.000000e+00
delta 0.000000e+00 4.995792e-01 0.000000e+00
delta 0.000000e+00 0.000000e+00 4.786953e-01
object 2 class gridconnections counts 353 193 257
object 3 class array type double rank 0 items 17509153         data follows
8.841046e-01 8.803156e-01 8.765030e-01
8.726683e-01 8.688033e-01 8.649116e-01
8.610003e-01 8.570672e-01 8.531058e-01
8.491277e-01 8.451333e-01 8.411144e-01
...
This is the general format, where first potential is of the format 
U(0,0,0) U(0,0,1) U(0,0,2)
U(0,0,3) U(0,0,4) U(0,0,5)
...

    The function reads the file and extracts the potential data at (i,j,k)
    """
    # Read the data
    with open(filepath) as f:
        data = f.readlines()
    l,b,h = 0,0,0
    ind=0
    # Extract length, width, height as l, b, h
    for line in data:
        ind+=1
        if line.startswith('object 3'):
            break
        elif line.startswith('object 1'):
            line= line.split()
            for i in range(len(line)):
                try:
                    if int(line[i]) and int(line[i]):
                        l = int(line[i])
                        b = int(line[i+1])
                        h = int(line[i+2])
                        break
                except:
                    pass
    #print("grid box: ", l,b,h)
    data = data[ind:]
    # Extract the potential data
    # Formula for which line to target 
    total_z = x * b * h + y * h + z
    # Calculate the line number and the position within the line
    line_number = total_z // 3 
    position = total_z % 3
    # Extract the potential from the data
    potential = data[line_number].split()[position]
    return potential

print(dx_pot_analyser(0,0,10,'codes/pot.dx'))
