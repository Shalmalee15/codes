# A code to multiply the second column in a plain data file
# A test for the GitHub repository

import numpy                   # Imports the numpy package

A = numpy.loadtxt("data.dat")  # Reads the data in the file named data.dat
#print A                       # Prints the data in data.dat stored in A 

A[:,1] *= 2.0 				         # Multiplies the second column in A by any number (Here, I took 2)

print A                        # Gives the desired output
