import numpy
import math


# from sympy import *
from random import *
from UnitVector import unitVector, magnitude

def rodriguesFormula(vecU, vecV, theta):

    vecU = unitVector(vecU, magnitude(vecV))

    rotation = (1 - math.cos(theta)) * numpy.dot(vecU, vecV) * vecU + (math.cos(theta) * vecV) + (math.sin(theta) * numpy.cross(vecU, vecV))

    return rotation

# def main():
#     vector = numpy.array([1, -1, 2])
#     uVector = numpy.array([0, 1/2, sqrt(3)/2])
#
#     theta = (math.pi / 3)
#
#     print(simplify(rodriguesFormula(uVector, vector, theta)))
#
# main()
