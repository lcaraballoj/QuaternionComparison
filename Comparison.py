import numpy
import math
import timeit
import pandas as pd
import matplotlib.pyplot as plt

from random import *
from prettytable import PrettyTable
from EulerAngle import X, Y, Z
from Quaternions import euler_to_quaternion

ITERATIONS = 100

# Function to graph all data
def graphAll(time):
    labels = ["Iteration", "Euler Time", "Quaternion Time"]     # Creating the labels

    eQTimeDict = dict(zip(labels, zip(*time)))                  # Create dictionary

    df = pd.DataFrame.from_dict(eQTimeDict)                # Use dictionary to create dataframs

    # Plotting graph
    df.plot.bar(x="Iteration", y=["Euler Time", "Quaternion Time"], stacked = True, width = 1)

    # Return the figure
    return plt.figure(1)

# Function to graph average times
def graphAvg(eTime, qTime):
    # Getting averages of compute time for euler and quaternion
    eAvg = numpy.average(eTime)
    qAvg = numpy.average(qTime)

    #Calculate standard deviation
    eStd = numpy.std(eTime)
    qStd = numpy.std(qTime)

    e = [min(eTime), max(eTime)]
    q = [min(qTime), max(qTime)]

    print(e)
    print(q)

    # Define labels, x_pos, values, error
    labels = ["Euler Average Time", "Quaternion Average Time"]
    x_pos = numpy.arange(len(labels))
    values = [eAvg, qAvg]
    error = [eStd, qStd]

    # Build the plot
    fig, ax = plt.subplots()
    ax.bar(x_pos, values,
       yerr=error,
       align='center',
       alpha=0.5,
       ecolor='black',
       capsize=10)
    ax.set_ylabel("Computation Time")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)
    ax.set_title("Computation Comparison")
    ax.yaxis.grid(True)

    # Return the figure
    return plt.figure(2)



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
