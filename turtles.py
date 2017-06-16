import numpy as np
import math as m
import matplotlib.pyplot as plt
turtleCommands=np.array([1,0.5*m.pi,1,0.5*m.pi,1,0.5*m.pi,1,0.5*m.pi])

def turtlePlot(turtleCommands):
    x=np.array([0,0])
    # Takes every second value starting from the second
    angles=turtleCommands[1::2]
    # Extra value inserted due to range in for loop
    angles=np.insert(angles, 0, 0) # (index, value)
    steps=turtleCommands[::2]
    steps=np.insert(steps, 0, 0) # (index, value)
    # Same number of d-values as number of angles
    dvalues = [0 for _ in angles]
    # Startvalue
    dvalues[0]=(np.array([1,0]))
    xvalues = [0 for _ in angles]
    xvalues[0]=(np.array([0,0]))
    # Calculating d- and x-values
    #Output = vector of coordinates
    for i in range(1,len(angles)):
        dvalues[i] = np.dot(np.array([[ m.cos(angles[i]), -m.sin(angles[i])],
               [m.sin(angles[i]), m.cos(angles[i])]]),dvalues[i-1])
        xvalues[i] = xvalues[i-1]+steps[i]*dvalues[i]
    print(xvalues)
    #Unpacks vector of datasets
    plt.plot(*zip(*xvalues)) # Plot line graph of x and y
    #Plottols
    plt.title("Din mor") #TODO
    # Set the title of the graph
    plt.xlabel("x-values") # Set the x-axis label
    plt.ylabel("y-values") # Set the y-axis label
    plt.xlim([-4, 4]) # Set the limits of the x-axis
    plt.ylim([-3, 3]) # Set the limits of the y-axis
    plt.grid()
    plt.show()
