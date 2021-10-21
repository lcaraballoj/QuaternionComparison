# Calculates a the unit vector given any random vector

import sympy
import numpy

# Calculate the magnitude
def magnitude(vector):
    magnitude = 0
    for i in range (vector.size):   # Keep doing operation till end of array
        magnitude += vector[i]**2  # Square each term and add it
        i += 1
    magnitude = sympy.sqrt(magnitude)   # Take the square root
    #print("Magnitude equals: ", magnitude)
    return magnitude    # Return magnitude value

# Calculate the unit vector
def unitVector(vector, magnitude):
    unitList = []   # Initialize unit vector list
    for i in range (vector.size):   # For all values in array
        unitList.append(vector[i]/magnitude)    # Take value and divide by magnitude and then add to list to calculate unit vector

    return(numpy.array(unitList))
