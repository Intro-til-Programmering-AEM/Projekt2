import numpy as np
import math as m
import matplotlib.pyplot as plt
import systems
from warning import max_vars
from systems import names


def turtleGraph(string, customSystem = None):
    # Is the string from the L-system for a Sierpinski triangle?
    # If there is input in customSystem, assign parameters accordingly
    if customSystem is not None:
        system = customSystem
        # The turns for the customSystem are set to 45 degrees left and right
        leftTurn = (1/4)*m.pi
        rightTurn = (-1/4)*m.pi
    # It must be the Sierpinski system if no customSystem has been defined
    # and there is in 'A' in the string
    elif 'A' in string:
        system = systems.sierpinski
        # The turns for Sierpinski are set to 30 degrees left and right
        leftTurn = (1/3)*m.pi
        rightTurn = (-1/3)*m.pi
        # Set scale factor
        scale_factor = 1/2
        # The maximum amount of variables returned is 3 per iteration
        vars_factor = 3
    # If none of the above, it's from the Koch curve
    else:
        system = systems.koch
        # The turns for Koch are set to 30 degrees left and 30 degrees right
        leftTurn = (1/3)*m.pi
        rightTurn = (-2/3)*m.pi
        # Set scale factor
        scale_factor = 1/3
        # The maximum amount of variables returned is 4 per iteration
        vars_factor = 4
    # Unpack the system into appropriate bits
    consts, _, rules, segment_symbols = system
    if customSystem is None:
        # Variables are the left side of the dictionary of the system
        variables = list(rules.keys())
        # Count the number of variables in the string
        num_vars = sum(string.count(v) for v in variables)
        # Figure out the scale by computing the scale_factor to the i'th power
        i = m.log(num_vars, vars_factor)
        scale = scale_factor**i
    # A custom made system won't be scaled
    else:
        scale = 1
    # Make an empty list to be filled with lengths and angles
    pairs = []
    # Translate the string to pairs of line_lengths and angles
    # Add a length of line every time one of the segment symbols is encountered
    # Otherwise add nothing
    # Translate all L's to leftTurns and R's to rightTurns
    for c in string:
        line_length = scale if c in segment_symbols else 0
        if c == 'L':
            angle = leftTurn
        elif c == 'R':
            angle = rightTurn
        else:
            angle = 0
        # Add them pairwise to the list pairs
        pairs.append(line_length)
        pairs.append(angle)
    return pairs

def turtlePlot(turtleCommands, name=None):
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
