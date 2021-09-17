import numpy
import math
import timeit
import pandas as pd
import matplotlib.pyplot as plt

from random import *
from prettytable import PrettyTable
from EulerAngle import X, Y, Z
from Quaternions import euler_to_quaternion
from Graphs import graphAll, graphAvg

ITERATIONS = 1000

def main():
    final = []
    time = []

    headers = ["phi", "theta", "psi", "Euler Rotation Matrix", "Time for Euler", "Time for Quaternion", "Quaternion Result"]
    table = PrettyTable(headers)

    i = 0

    while i<=ITERATIONS:
        startEuler = timeit.default_timer()          # Start timer for euler caluclation run time

        #Generate random angles
        phi = math.pi / randint(1, 6)
        theta = math.pi / randint(1, 6)
        psi = math.pi / randint(1, 6)

        #print("phi = ", phi)
        #print("theta = ", theta)
        #print("psi = ", psi)

        euler = X(phi) * Y(theta) * Z(theta)       # Calculate rotation matrix
        stopEuler = timeit.default_timer()         # Stop timer for euler calculation run time

        #print("\n", numpy.round(euler, decimals = 2))       # Print rotation matrix
        #print("\nTime: ", stopEuler - startEuler, "\n")     # Print run time

        startQuaternion = timeit.default_timer()

        quaternion = euler_to_quaternion(phi, theta, psi)
        stopQuaternion = timeit.default_timer()             # Stop timer for run time

        #print("\n", numpy.round(quaternion, decimals = 2))      # Print rotation matrix
        #print("\nTime: ", stopQuaternion - startQuaternion)     # Print run time

        add = table.add_row([phi, theta, psi, numpy.round(euler, decimals = 2), stopEuler - startEuler, stopQuaternion - startQuaternion, numpy.round(quaternion, decimals  = 2)])  #Add information to table

        result = [phi, theta, psi, euler, stopEuler - startEuler, stopQuaternion - startQuaternion, quaternion]              # Add information to first array

        final.append(result)            #Append first array to final array

        eQTime = [i, stopEuler - startEuler, stopQuaternion - startQuaternion]

        eTime = [stopEuler - startEuler]
        qTime = [stopQuaternion - startQuaternion]

        time.append(eQTime)

        i += 1

    print(table)

    dictionary = dict(zip(headers, zip(*final)))    # Convert final array to a dictionary

    dfTable = pd.DataFrame.from_dict(dictionary)                            # Define the dataframes
    dfTable.to_csv("Comparison.csv", index = False, header = True)         # Write dataframes to csv to be saved

    graphAll(time)
    graphAvg(eTime, qTime)

    plt.show()

main()
