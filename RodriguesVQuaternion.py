import numpy
import timeit
import pandas as pd
import matplotlib.pyplot as plt

from sympy import *
from random import *
from prettytable import PrettyTable
from Rodrigues import rodriguesFormula
from Quaternions import calcQuaternion, quaternionRotation
from Graphs import graphAllRodriguesQuaternions, graphAvgRodriguesQuaternions

ITERATIONS = 20

def main():
    final = []
    time = []

    headers = ["theta", "Rodrigues Formula ", "Time for Rodrigues", "Time for Quaternion", "Quaternion Result"]
    table = PrettyTable(headers)

    i = 0

    while i<=ITERATIONS:
        # Generate random angles
        theta = pi / 6

        # Generate vectors
        # v = [1, -1, 2]
        # u = [0, 1/2, sqrt(3)/2]

        u = [randint(1, 10), randint(1, 10), randint(1, 10)]
        v = [randint(1, 10), randint(1, 10), randint(1, 10)]

        startRodrigues = timeit.default_timer()          # Start timer for Rodrigues caluclation run time

        rodrigues = rodriguesFormula(numpy.array(u), numpy.array(v), theta)

        stopRodrigues = timeit.default_timer()         # Stop timer for Rodrigues calculation run time

        u.insert(0, 0)
        v.insert(0,0)

        q = calcQuaternion(numpy.array(u), theta)

        startQuaternion = timeit.default_timer()

        quaternion = quaternionRotation(q, numpy.array(v), theta)

        #quaternion = quaternionRotation(numpy.array(u), numpy.array(v), theta)

        stopQuaternion = timeit.default_timer()             # Stop timer for run time

        # Add value to table
        add = table.add_row([theta, rodrigues, stopRodrigues - startRodrigues, stopQuaternion - startQuaternion, quaternion])  # Add information to table

        result = [theta, stopRodrigues - startRodrigues, stopQuaternion - startQuaternion, quaternion]              # Add information to first array

        final.append(result)            #Append first array to final array

        rQTime = [i, stopRodrigues - startRodrigues, stopQuaternion - startQuaternion]

        rTime = [stopRodrigues- startRodrigues]
        qTime = [stopQuaternion - startQuaternion]

        time.append(rQTime)

        i += 1

    print(table)

    dictionary = dict(zip(headers, zip(*final)))    # Convert final array to a dictionary

    dfTable = pd.DataFrame.from_dict(dictionary)                            # Define the dataframes
    dfTable.to_csv("Comparison.csv", index = False, header = True)         # Write dataframes to csv to be saved

    graphAllRodriguesQuaternions(time)
    graphAvgRodriguesQuaternions(rTime, qTime)

    plt.show()

main()
