import numpy
import math
import timeit
import pandas as pd
import matplotlib.pyplot as plt

from random import *
from prettytable import PrettyTable
from EulerAngle import X, Y, Z
from Quaternions import euler_to_quaternion

ITERATIONS = 200

# importing pandas library
import pandas as pd
# import matplotlib library
import matplotlib.pyplot as plt

'''
def label_array():
    array = []
    i = 0
    while i<=ITERATIONS:
        array.append(i)

    return array


def graph(labels, eTime, qTime):
    xaxisLabels = labels

    eData = eTime
    qData = qTime


    x = np.arrange(len(labels))
    width = 0.2

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, eTime, width, label='Euler Time')
    rects2 = ax.bar(x + width/2, qTime, width, label='Quaternion Time')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Compute Time')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()
'''


def main():
    final = []
    time = []

    headers = ["phi", "theta", "psi", "Euler Rotation Matrix", "Time for Euler", "Time for Quaternion", "Quaternion Result"]
    table = PrettyTable(headers)

    i = 0

    while i<=ITERATIONS:
        startEuler = timeit.default_timer()          #Start timer for euler caluclation run time

        #Generate random angles
        phi = math.pi / randint(1, 6)
        theta = math.pi / randint(1, 6)
        psi = math.pi / randint(1, 6)

        #print("phi = ", phi)
        #print("theta = ", theta)
        #print("psi = ", psi)

        euler = X(phi) * Y(theta) * Z(theta)       #Calculate rotation matrix
        stopEuler = timeit.default_timer()         #Stop timer for euler calculation run time

        #print("\n", numpy.round(euler, decimals = 2))       #Print rotation matrix
        #print("\nTime: ", stopEuler - startEuler, "\n")     #Print run time

        startQuaternion = timeit.default_timer()

        quaternion = euler_to_quaternion(phi, theta, psi)
        stopQuaternion = timeit.default_timer()             #Stop timer for run time

        #print("\n", numpy.round(quaternion, decimals = 2))      #Print rotation matrix
        #print("\nTime: ", stopQuaternion - startQuaternion)     #Print run time

        add = table.add_row([phi, theta, psi, numpy.round(euler, decimals = 2), stopEuler - startEuler, stopQuaternion - startQuaternion, numpy.round(quaternion, decimals  = 2)])  #Add information to table

        result = [phi, theta, psi, euler, stopEuler - startEuler, stopQuaternion - startQuaternion, quaternion]              #Add information to first array

        final.append(result)            #Append first array to final array

        eQTime = [i, stopEuler - startEuler, stopQuaternion - startQuaternion]

        time.append(eQTime)

        i += 1

    print(table)

    dictionary = dict(zip(headers, zip(*final)))    #Convert final array to a dictionary

    dfTable = pd.DataFrame.from_dict(dictionary)                            #Define the dataframes
    dfTable.to_csv("Comparison.csv", index = False, header = True)         #Write dataframes to csv to be saved

    labels = ["Iteration", "Euler Time", "Quaternion Time"]

    eQTimeDict = dict(zip(labels, zip(*time)))

    dfGraph = pd.DataFrame.from_dict(eQTimeDict)

    print(dfGraph)
    #print(dfTable)

    # plotting graph
    dfGraph.plot(x="Iteration", y=["Euler Time", "Quaternion Time"], kind="bar", width = 1)

    plt.show()

    #graph(label_array(), eTime, qTime)

main()
