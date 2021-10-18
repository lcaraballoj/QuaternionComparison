#https://personal.utdallas.edu/~sxb027100/dock/quaternion.html

import math as m
import numpy as np
import timeit
from sympy import sin, cos, pi

from random import *

from UnitVector import unitVector, magnitude

#To calculate quaternion multiple the quaternion by a vector by the conjugate

#Calculate the conjugate
def conjugate(q):
    q[1] = - q[1]
    q[2] = -q[2]
    q[3] = -q[3]

    print ("Conjugate: ", q)
    return q

def quaternion(uVector, theta):
    u = unitVector(uVector, magnitude(uVector))

    print("Unit Vector: ", u)

    q = cos(theta/2) + (sin(theta/2) * uVector)

    print("Quaternion: ", q)

    return u

def quaternionMultiplication(q1, q2):
    product = []
    product.append(q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3])
    product.append(q1[0]*q2[1] + q1[1]*q2[0] + q1[2]*q2[3] - q1[3]*q2[2])
    product.append(q1[0]*q2[2] + q1[2]*q2[0] + q1[3]*q2[1] - q1[1]*q2[3])
    product.append(q1[0]*q2[3] + q1[3]*q2[0] + q1[1]*q2[2] - q1[2]*q2[1])

    return product

def quaternionRotation(vector, uVector, theta):
    q = quaternion(uVector, theta)
    print ("Quaternion: ", q)
    rotation = quaternionMultiplication(q, vector)
    print (rotation)
    rotation = quaternionMultiplication(rotation, conjugate(q))

    return rotation


def euler_to_quaternion(phi, theta, psi):

        qw = cos(phi/2) * cos(theta/2) * cos(psi/2) + sin(phi/2) * sin(theta/2) * sin(psi/2)
        qx = sin(phi/2) * cos(theta/2) * cos(psi/2) - cos(phi/2) * sin(theta/2) * sin(psi/2)
        qy = cos(phi/2) * sin(theta/2) * cos(psi/2) + sin(phi/2) * cos(theta/2) * sin(psi/2)
        qz = cos(phi/2) * cos(theta/2) * sin(psi/2) - sin(phi/2) * sin(theta/2) * cos(psi/2)

        return [qw, qx, qy, qz]


def mult():
    q1 = np.array([0, 0, 1, 0])
    q2 = np.array([0, 1, 0, 0])

    print(quaternionMultiplication(q1, q2))

#mult()

def main():
    theta = (pi)
    print("Theta: ", theta)
    vector = np.array([0, 0, 1, 0])
    uVector = np.array([0, 1, 0, 0])

    print(quaternionRotation(vector, uVector, theta))

main()

'''
def main():
    i = 0
    while i < 5:
        start = timeit.default_timer()          #Start timer for run time

        #Generate random angles
        phi = m.pi / randint(1, 100)
        theta = m.pi / randint(1, 100)
        psi = m.pi / randint(1, 100)

        print("phi = ", phi)
        print("theta = ", theta)
        print("psi = ", psi)

        R = euler_to_quaternion(phi, theta, psi)
        stop = timeit.default_timer()          #Stop timer for run time

        print("\n", numpy.round(R, decimals = 2))   #Print rotation matrix
        print("\nTime: ", stop - start)             #Print run time

        i += 1
'''

#main()
