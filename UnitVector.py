# import math
import sympy

def magnitude(vector):
    magnitude = 0
    for i in range (vector.size):
        magnitude += sympy.sqrt(vector[i]**2)
        i += 1

    #print("Magnitude equals: ", magnitude)
    return magnitude

def unitVector(vector, magnitude):
    unitList = []
    for i in range (vector.size):
        unitList.append(vector[i]/magnitude)

    return(unitList)

# def main():
#     list = [0, 1, 1, 1]
#     array = np.array(list)
#
#     print(unitVector(array, magnitude(array)))
#
#
# main()
