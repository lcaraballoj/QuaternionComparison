# To calculate a quaternion representing rotation using two different methods.

import numpy as np
import timeit
from sympy import sin, cos, pi, sqrt, simplify

from random import *

from UnitVector import unitVector, magnitude

# Calculates the conjugate
def conjugate(q):
    q[0] = q[0]
    q[1] = - q[1]
    q[2] = -q[2]
    q[3] = -q[3]

    print ("Conjugate: ", q)
    return q

# Calculates the quaternion
def quaternion(uVector, theta):
    u = unitVector(uVector, magnitude(uVector))     # Get the unit vector

    #print("Unit Vector: ", u)       # Print the unit vector (debugging)

    angle = theta/2

    q = [cos(angle)]      # Obtain the scalar part of the quaternion

    for x in range (1, uVector.size):           # Append values for vector
        value = uVector[x] * sin(angle)         # For each value in the unit vector multiply it my sin(angle), where angle = (theta/2)
        q.append(value)                         # Append value to quaternion

    return (np.array(q))    # Return the quaternion calculated

# Follow the rules to multiply quaternions (general formulation from using relations for i, j, k)
def quaternionMultiplication(q1, q2):
    product = []    # Create list to convert to array/vector
    product.append(q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3])
    product.append(q1[0]*q2[1] + q1[1]*q2[0] + q1[2]*q2[3] - q1[3]*q2[2])
    product.append(q1[0]*q2[2] + q1[2]*q2[0] + q1[3]*q2[1] - q1[1]*q2[3])
    product.append(q1[0]*q2[3] + q1[3]*q2[0] + q1[1]*q2[2] - q1[2]*q2[1])

    return np.array(product)    # Return the vector

# Function to caluclate the rotarion quaternion given two vectors and an angle
def quaternionRotation(vector, uVector, theta):
    q = quaternion(uVector, theta)      # Find the quaternion
    print ("Quaternion: ", q)   # Print the quaternion(debug)
    rotation = quaternionMultiplication(quaternionMultiplication(q, vector), conjugate(q))  # Caluclate the quaternion that represents the rotation

    return rotation     # Retuarn rotation quaternion

# Function to calculate the quaternion given three Euler angles
def euler_to_quaternion(phi, theta, psi):
        qw = cos(phi/2) * cos(theta/2) * cos(psi/2) + sin(phi/2) * sin(theta/2) * sin(psi/2)    # Calculate scalar
        qx = sin(phi/2) * cos(theta/2) * cos(psi/2) - cos(phi/2) * sin(theta/2) * sin(psi/2)    # Calculate i
        qy = cos(phi/2) * sin(theta/2) * cos(psi/2) + sin(phi/2) * cos(theta/2) * sin(psi/2)    # Calculate j
        qz = cos(phi/2) * cos(theta/2) * sin(psi/2) - sin(phi/2) * sin(theta/2) * cos(psi/2)    # Calculate k

        return [qw, qx, qy, qz] # Combine s, i, j, k to obtain quaternion

def main():
    theta = pi/4
    #print("Theta: ", theta)
    vector = np.array([0, 1, 0, 0])
    uVector = np.array([0, 0.0, 1, 0.0])

    print("Answer: ", simplify(quaternionRotation(vector, uVector, theta)))

main()
