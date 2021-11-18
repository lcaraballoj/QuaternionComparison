import numpy
import timeit
import math
import pandas as pd
import matplotlib.pyplot as plt

from random import *
from prettytable import PrettyTable
from Rodrigues import rodrigues_formula
from Quaternions import calc_quaternion, quaternion_rotation
from Graphs import graph_all_rodrigues_quaternions, graph_avg_rodrigues_quaternions

ITERATIONS = 20     #Number of times that operations will run

def main():
    # Initialize arrays
    final = []
    time = []

    headers = ["theta", "Rodrigues Formula ", "Time for Rodrigues", "Time for Quaternion", "Quaternion Result"]     # Headers for table
    table = PrettyTable(headers)

    i = 0

    while i<=ITERATIONS:    # Loop (depends on ITERATIONS constant at top)
        # Generate random angles
        theta = math.pi / randint(1, 6)      # Random angle

        # Generate vectors
        # v = [1, -1, 2]
        # u = [0, 1/2, sqrt(3)/2]

        # Random values for both vectors u and v
        u = [randint(1, 10), randint(1, 10), randint(1, 10)]
        v = [randint(1, 10), randint(1, 10), randint(1, 10)]

        startRodrigues = timeit.default_timer()          # Start timer for Rodrigues caluclation run time

        rodrigues = rodrigues_formula(numpy.array(u), numpy.array(v), theta)     # Run Rodrigues' rotation formula

        stopRodrigues = timeit.default_timer()         # Stop timer for Rodrigues calculation run time

        u.insert(0, 0)      # Add scalar of 0
        v.insert(0, 0)       # Add scalar of 0

        q = calc_quaternion(numpy.array(u), theta)       # Generate the quaternion

        startQuaternion = timeit.default_timer()        # Start timer for quaternion calculation run time

        quaternion = quaternion_rotation(q, numpy.array(v), theta)       # Generate quaternion to describe the rotation

        #quaternion = quaternionRotation(numpy.array(u), numpy.array(v), theta)

        stopQuaternion = timeit.default_timer()             # Stop timer for quaternion calculation run time
        print (stopQuaternion-startQuaternion)

        # Add value to table
        add = table.add_row([theta, rodrigues, stopRodrigues - startRodrigues, stopQuaternion - startQuaternion, quaternion])

        result = [theta, rodrigues, stopRodrigues - startRodrigues, stopQuaternion - startQuaternion, quaternion]              # Add information to first array

        final.append(result)            #Append first array to final array

        rQTime = [i, stopRodrigues - startRodrigues, stopQuaternion - startQuaternion]      # List to hold iteration number and run time data

        rTime = [stopRodrigues- startRodrigues]     # List to hold run time data for Rodrigues
        qTime = [stopQuaternion - startQuaternion]  # List to hold run time data for quaternions

        time.append(rQTime)

        i += 1      # Move on to next iteration

    print(table)

    dictionary = dict(zip(headers, zip(*final)))    # Convert final array to a dictionary

    dfTable = pd.DataFrame.from_dict(dictionary)                                     # Define the dataframes
    dfTable.to_csv("RodriguesVQuaternion.csv", index = False, header = True)         # Write dataframes to csv to be saved

    graph_all_rodrigues_quaternions(time)              # Graph data for all iterations
    graph_avg_rodrigues_quaternions(rTime, qTime)      # Graph data for average of all iterations

    plt.show()      # Display graphs

main()
