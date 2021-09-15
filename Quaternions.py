#https://personal.utdallas.edu/~sxb027100/dock/quaternion.html

import math as m
import numpy
import timeit

from random import *

#To calculate quaternion multiple the quaternion by a vector by the conjugate

#Calculate the conjugate
def conjugate(q):
    s, a, b, c = q
    return(s, -a, -b, -c)

def qv_multiply(q1, v1):
    q2 = (0.0) + v1     #A pure quaternion is purely the vector part
    return q_multiply(q_multiply(q1, q2), q_conjugate(q1))[1:]

#Multiply two quaternions for rotation and to get a rotation matrix

def q_multiply():
    s1, a1, b1, c1 = q1
    s2, a2, b2, c2 = q2

    #Calculation for different components
    s = (s1*s2 - a1*a2 - b1*b2 - c1*c2)
    a = (s1*a2 + a1*s2 + b1*c2 - c1*b2)
    b = (s1*b2 - a1*c2 + b1*s2 + c1*a2)
    c = (s1*c2 + a1*b2 - b1*a2 + c1*s2)

    return s, a, b, c

#Multiply all components together to get result
def main():
    q = q_multiply(q_multiply(q1, q2), q_conjugate(q1))[1:]

    print(q)

def euler_to_quaternion(phi, theta, psi):

        qw = m.cos(phi/2) * m.cos(theta/2) * m.cos(psi/2) + m.sin(phi/2) * m.sin(theta/2) * m.sin(psi/2)
        qx = m.sin(phi/2) * m.cos(theta/2) * m.cos(psi/2) - m.cos(phi/2) * m.sin(theta/2) * m.sin(psi/2)
        qy = m.cos(phi/2) * m.sin(theta/2) * m.cos(psi/2) + m.sin(phi/2) * m.cos(theta/2) * m.sin(psi/2)
        qz = m.cos(phi/2) * m.cos(theta/2) * m.sin(psi/2) - m.sin(phi/2) * m.sin(theta/2) * m.cos(psi/2)

        return [qw, qx, qy, qz]


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

main()
