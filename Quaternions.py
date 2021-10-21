# To calculate a quaternion representing rotation using two different methods.

import timeit
import math
import numpy as np

# from sympy import *
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
def calcQuaternion(uVector, theta):
    u = unitVector(uVector, magnitude(uVector))     # Get the unit vector

    #print("Unit Vector: ", u)       # Print the unit vector (debugging)

    angle = theta/2

    q = [math.cos(angle)]      # Obtain the scalar part of the quaternion

    for x in range (1, uVector.size):           # Append values for vector
        value = uVector[x] * math.sin(angle)         # For each value in the unit vector multiply it my sin(angle), where angle = (theta/2)
        q.append(value)                         # Append value to quaternion

    return (np.array(q))    # Return the quaternion calculated

# Follow the rules to multiply quaternions (general formulation from using relations for i, j, k)
def quaternionMultiplication(q1, q2):
    product = []    # Create list to convert to array/vector
    product.append(q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3])       # s
    product.append(q1[0]*q2[1] + q1[1]*q2[0] + q1[2]*q2[3] - q1[3]*q2[2])       # i
    product.append(q1[0]*q2[2] + q1[2]*q2[0] + q1[3]*q2[1] - q1[1]*q2[3])       # j
    product.append(q1[0]*q2[3] + q1[3]*q2[0] + q1[1]*q2[2] - q1[2]*q2[1])       # k

    return np.array(product)    # Return the quaternion (s, ai, bj, ck)

# Function to caluclate the rotation quaternion given two vectors and an angle
def quaternionRotationConvert(uVector, vector, theta):
    q = calcQuaternion(uVector, theta)      # Find the quaternion
    print ("Quaternion: ", q)           # Print the quaternion(debug)
    rotation = quaternionMultiplication(quaternionMultiplication(q, vector), conjugate(q))  # Caluclate the quaternion that represents the rotation

    return rotation     # Retuarn rotation quaternion

# Function that does not take into account the time to generate the quaternion
def quaternionRotation(q, v, theta):
    rotation = quaternionMultiplication(quaternionMultiplication(q, v), conjugate(q))  # Caluclate the quaternion that represents the rotation

    return rotation     # Return rotation quaternion


# Function to calculate the quaternion given three Euler angles
def euler_to_quaternion(phi, theta, psi):
        qw = math.cos(phi/2) * math.cos(theta/2) * math.cos(psi/2) + math.sin(phi/2) * math.sin(theta/2) * math.sin(psi/2)    # Calculate scalar
        qx = math.sin(phi/2) * math.cos(theta/2) * math.cos(psi/2) - math.cos(phi/2) * math.sin(theta/2) * math.sin(psi/2)    # Calculate i
        qy = math.cos(phi/2) * math.sin(theta/2) * math.cos(psi/2) + math.sin(phi/2) * math.cos(theta/2) * math.sin(psi/2)    # Calculate j
        qz = math.cos(phi/2) * math.cos(theta/2) * math.sin(psi/2) - math.sin(phi/2) * math.sin(theta/2) * math.cos(psi/2)    # Calculate k

        return [qw, qx, qy, qz] # Combine s, i, j, k to obtain quaternion
