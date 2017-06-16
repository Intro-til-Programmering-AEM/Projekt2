import numpy as np
import math as m
import matplotlib.pyplot as plt
import systems

def turtleGraph(string):
    leftTurn = (1/3)*m.pi
    # Is the string from the L-system for a Sierpinski triangle?
    if 'A' in string:
        system = systems.sierpinski
        rightTurn = (-1/3)*m.pi
        scale_factor = 1/2
        vars_factor = 3
    # If not, it's from the Koch curve
    else:
        system = systems.koch
        rightTurn = (-2/3)*m.pi
        scale_factor = 1/3
        vars_factor = 4
    num_vars = sum(string.count(v) for v in system[0])
    i = m.log(num_vars, vars_factor)
    scale = scale_factor**i
    string = filter(lambda c: c in ['R','L'], string)
    return [(scale,rightTurn if c == 'R' else leftTurn) for c in string]

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
