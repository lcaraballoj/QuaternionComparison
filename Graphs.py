import numpy
import pandas as pd
import matplotlib.pyplot as plt

# Function to graph all data
def graphAll(time):

    labels = ["Iteration", "Euler Time", "Quaternion Time"]     # Creating the labels

    eQTimeDict = dict(zip(labels, zip(*time)))                  # Create dictionary

    df = pd.DataFrame.from_dict(eQTimeDict)                # Use dictionary to create dataframes

    # Plotting graph
    graph = df.plot.bar(x="Iteration", y=["Euler Time", "Quaternion Time"], width=1, title="Rotation Matrix vs. Quaternion Compute Time")
    graph.set_title("Rotation Matrix vs. Quaternion Compute Time", fontdict={'fontsize':18})
    graph.set_ylabel("Compute Time", fontdict={'fontsize':18})
    graph.set_xlabel("Iteration", fontdict={'fontsize':18})
    graph.legend(fontsize=18)

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
    ax.set_title("Average Computation Comparison")
    ax.yaxis.grid(True)

    # Return the figure
    return plt.figure(2)


# Function to graph all data
def graphAllRodriguesQuaternions(time):

    labels = ["Iteration", "Rodrigues Time", "Quaternion Time"]     # Creating the labels

    eQTimeDict = dict(zip(labels, zip(*time)))                  # Create dictionary

    df = pd.DataFrame.from_dict(eQTimeDict)                # Use dictionary to create dataframes

    # Plotting graph
    graph = df.plot.bar(x="Iteration", y=["Rodrigues Time", "Quaternion Time"], width=1, title="Rotation Matrix vs. Quaternion Compute Time")
    graph.set_title("Rodrigues Rotation vs. Quaternion Compute Time", fontdict={'fontsize':18})
    graph.set_ylabel("Compute Time", fontdict={'fontsize':18})
    graph.set_xlabel("Iteration", fontdict={'fontsize':18})
    graph.legend(fontsize=18)

    # Return the figure
    return plt.figure(1)

# Function to graph average times
def graphAvgRodriguesQuaternions(rTime, qTime):
    # Getting averages of compute time for euler and quaternion
    rAvg = numpy.average(rTime)
    qAvg = numpy.average(qTime)

    #Calculate standard deviation
    rStd = numpy.std(rTime)
    qStd = numpy.std(qTime)

    r = [min(rTime), max(rTime)]
    q = [min(qTime), max(qTime)]

    # Define labels, x_pos, values, error
    labels = ["Rodrigues Average Time", "Quaternion Average Time"]
    x_pos = numpy.arange(len(labels))
    values = [rAvg, qAvg]
    error = [rStd, qStd]

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
    ax.set_title("Average Computation Comparison")
    ax.yaxis.grid(True)

    # Return the figure
    return plt.figure(2)
