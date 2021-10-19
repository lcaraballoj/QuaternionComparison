import numpy
import math

from random import *
from UnitVector import unitVector

def rodriguesFormula(vecU, vecV, theta):

    rotation = (1 - math.cos(theta)) * numpy.dot(vecU, vecV) * vecU + (math.cos(theta) * vecV) + (math.sin(theta) * numpy.cross(vecU, vecV))

    return rotation

# def main():
#     listU = [(3/(5 * math.sqrt(2))), ((2* math.sqrt(2))/5), (-1 / math.sqrt(2))]
#     listV = [2, 3, -1]
#
#     theta = (math.pi / 3)
#
#     print(rodriguesFormula(listU, listV, theta))
#
# main()
