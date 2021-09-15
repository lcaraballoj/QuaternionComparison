import numpy
import math
import timeit

from random import *

#Create matrix for the x-axis
def X(theta):
    return numpy.matrix([[1, 0, 0],
                         [0, math.cos(theta), -math.sin(theta)],
                         [0, math.sin(theta), math.cos(theta)]])

#Create matrix for the y-axis
def Y(theta):
    return numpy.matrix([[math.cos(theta), 0, -math.sin(theta)],
                         [0, 1, 0],
                         [-math.sin(theta), 0, math.cos(theta)]])

#Create matrix for the z-axis
def Z(theta):
    return numpy.matrix([[math.cos(theta), -math.sin(theta), 0],
                         [math.sin(theta), -math.cos(theta), 0],
                         [0, 0, 1]])

def main():
    start = timeit.default_timer()          #Start timer for run time

    #Generate random angles
    phi = math.pi / randint(1, 100)
    theta = math.pi / randint(1, 100)
    psi = math.pi / randint(1, 100)

    print("phi = ", phi)
    print("theta = ", theta)
    print("psi = ", psi)

    R = X(phi) * Y(theta) * Z(theta)       #Calculate rotation matrix
    stop = timeit.default_timer()          #Stop timer for run time

    print("\n", numpy.round(R, decimals = 2))   #Print rotation matrix
    print("\nTime: ", stop - start)             #Print run time

main()
