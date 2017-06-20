import numpy as np
import math as m
import matplotlib.pyplot as plt
import systems
from warning import max_vars
from systems import names


def turtleGraph(string, customSystem = None):
    # Is the string from the L-system for a Sierpinski triangle?
    if customSystem is not None:
        system = customSystem
        leftTurn = (1/4)*m.pi
        rightTurn = (-1/4)*m.pi
        scale_factor = 1
        vars_factor = max_vars(system)
    elif 'A' in string:
        system = systems.sierpinski
        leftTurn = (1/3)*m.pi
        rightTurn = (-1/3)*m.pi
        scale_factor = 1/2
        vars_factor = 3
    # If not, it's from the Koch curve
    else:
        system = systems.koch
        leftTurn = (1/3)*m.pi
        rightTurn = (-2/3)*m.pi
        scale_factor = 1/3
        vars_factor = 4
    consts, _, rules, segment_symbols = system
    variables = list(rules.keys())
    num_vars = sum(string.count(v) for v in variables)
    if vars_factor == 1:
        i = 1
    else:
        i = m.log(num_vars, vars_factor)
    scale = scale_factor**i
    pairs = []
    for c in string:
        line_length = scale if c in segment_symbols else 0
        if c == 'L':
            angle = leftTurn
        elif c == 'R':
            angle = rightTurn
        else:
            angle = 0
        pairs.append(line_length)
        pairs.append(angle)
    return pairs

def turtlePlot(turtleCommands):
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
    # Output = vector of coordinates
    for i in range(1,len(angles)):
        dvalues[i] = np.dot(np.array([[ m.cos(angles[i]), -m.sin(angles[i])],
               [m.sin(angles[i]), m.cos(angles[i])]]),dvalues[i-1])
        xvalues[i] = xvalues[i-1]+steps[i]*dvalues[i]
    # Unpacks vector of datasets
    plt.plot(*zip(*xvalues)) # Plot line graph of x and y
    # Plottols
    if name is not None:
        plt.title(name) # TODO optionally include name of system
    else:
        plt.title("Your plot of choice:")
    plt.show()
