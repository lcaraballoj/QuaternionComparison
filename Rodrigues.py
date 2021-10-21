import numpy
import math


# from sympy import *
from random import *
from UnitVector import unitVector, magnitude

def rodriguesFormula(vecU, vecV, theta):

    vecU = unitVector(vecU, magnitude(vecV))

    rotation = (1 - math.cos(theta)) * numpy.dot(vecU, vecV) * vecU + (math.cos(theta) * vecV) + (math.sin(theta) * numpy.cross(vecU, vecV))

    return rotation
