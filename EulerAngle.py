import numpy
import math
import timeit

from random import *

#Create matrix for the x-axis
def X(theta):
    cosine = math.cos(theta)
    sine = math.sin(theta)
    return numpy.matrix([[1, 0, 0],
                         [0, cosine, -sine],
                         [0, sine, cosine]])

#Create matrix for the y-axis
def Y(theta):
    cosine = math.cos(theta)
    sine = math.sin(theta)
    return numpy.matrix([[cosine, 0, sine],
                         [0, 1, 0],
                         [-sine, 0, cosine]])

#Create matrix for the z-axis
def Z(theta):
    cosine = math.cos(theta)
    sine = math.sin(theta)
    return numpy.matrix([[cosine, -sine, 0],
                         [sine, cosine, 0],
                         [0, 0, 1]])
