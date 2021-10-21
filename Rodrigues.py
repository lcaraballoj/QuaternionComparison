import numpy
import math


# from sympy import *
from random import *
from UnitVector import unit_vector, magnitude

def rodrigues_formula(vecU, vecV, theta):

    vecU = unit_vector(vecU, magnitude(vecV))

    rotation = (1 - math.cos(theta)) * numpy.dot(vecU, vecV) * vecU + (math.cos(theta) * vecV) + (math.sin(theta) * numpy.cross(vecU, vecV))

    return rotation
