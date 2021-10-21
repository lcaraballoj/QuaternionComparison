import numpy
import math
import timeit
import pandas as pd
import matplotlib.pyplot as plt

from random import *
from prettytable import PrettyTable
from EulerAngle import X, Y, Z
from Quaternions import euler_to_quaternion
from Graphs import graph_all_euler_quaternions, graph_avg_euler_quaternions

ITERATIONS = 20

def main():
    final = []
    time = []

    headers = ["phi", "theta", "psi", "Euler Rotation Matrix", "Time for Euler", "Time for Quaternion", "Quaternion Result"]    # Headers for table
    table = PrettyTable(headers)        # Genearte table

    i = 0       # Initialize iteration

    while i<=ITERATIONS:                             # Loop (depends on ITERATIONS constant at top)
        startEuler = timeit.default_timer()          # Start timer for euler caluclation run time

        #Generate random angles
        phi = math.pi / randint(1, 6)
        theta = math.pi / randint(1, 6)
        psi = math.pi / randint(1, 6)

        euler = X(phi) * Y(theta) * Z(theta)       # Calculate rotation matrix
        stopEuler = timeit.default_timer()         # Stop timer for euler calculation run time

        startQuaternion = timeit.default_timer()

        quaternion = euler_to_quaternion(phi, theta, psi)

        stopQuaternion = timeit.default_timer()             # Stop timer for run time

        add = table.add_row([phi, theta, psi, numpy.round(euler, decimals = 2), stopEuler - startEuler, stopQuaternion - startQuaternion, numpy.round(quaternion, decimals  = 2)])  #Add information to table

        result = [phi, theta, psi, euler, stopEuler - startEuler, stopQuaternion - startQuaternion, quaternion]              # Add information to first array

        final.append(result)            #Append first array to final array

        eQTime = [i, stopEuler - startEuler, stopQuaternion - startQuaternion]      # List to hold iteration number and run time data

        eTime = [stopEuler - startEuler]                # List to hold run time data for Euler
        qTime = [stopQuaternion - startQuaternion]      # List to hold run time data for quaternions

        time.append(eQTime)

        i += 1          # Move on to next iteration

    print(table)

    dictionary = dict(zip(headers, zip(*final)))    # Convert final array to a dictionary

    dfTable = pd.DataFrame.from_dict(dictionary)                            # Define the dataframes
    dfTable.to_csv("Comparison.csv", index = False, header = True)         # Write dataframes to csv to be saved

    graph_all_euler_quaternions(time)               # Graph data for all iterations
    graph_avg_euler_quaternions(eTime, qTime)       # Graph data for average of all iterations

    plt.show()

main()
