import numpy
import math
import timeit

from random import *
from EulerAngle import X, Y, Z
from Quaternions import euler_to_quaternion

def main():
        i = 0
        while i<=5:
            startEuler = timeit.default_timer()          #Start timer for run time

            #Generate random angles
            phi = math.pi / randint(1, 100)
            theta = math.pi / randint(1, 100)
            psi = math.pi / randint(1, 100)

            print("phi = ", phi)
            print("theta = ", theta)
            print("psi = ", psi)

            euler = X(phi) * Y(theta) * Z(theta)       #Calculate rotation matrix
            stopEuler = timeit.default_timer()          #Stop timer for run time

            print("\n", numpy.round(euler, decimals = 2))   #Print rotation matrix
            print("\nTime: ", stopEuler - startEuler, "\n")             #Print run time

            startQuaternion = timeit.default_timer()

            quaternion = euler_to_quaternion(phi, theta, psi)
            stopQuaternion = timeit.default_timer()          #Stop timer for run time

            print("\n", numpy.round(quaternion, decimals = 2))   #Print rotation matrix
            print("\nTime: ", stopQuaternion - startQuaternion)             #Print run time

            i += 1

main()
