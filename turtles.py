import numpy as np
import math as m
import matplotlib.pyplot as plt
import systems
from systems import names, max_vars

# Generates a list that contains the line lengths and turn angles
# that the system gives rise to,
# detecting the system identity among the predefined system
# unless a custom system was used
# Inputs: a string `string` resulting from iterating an L-system;
# optionally a tuple `customSystem` describing the custom system
# that generated `string`, if any.
# Output: a list of line lengths followed by turn angles,
# representing the movement necessary to plot `string`.
# Assumptions: `string` is a valid string, i.e.
# iterating one of the predefined L-systems,
# or, if given, the custom L-system
# could have produced `string`.
def turtleGraph(string, customSystem = None):
    if customSystem is not None:
        system = customSystem
        # The turns for the customSystem are set to 45 degrees left and right
        leftTurn = (1/4)*m.pi
        rightTurn = (-1/4)*m.pi
    # If no customSystem has been defined
    # it has to be a predefined system.
    # The Sierpinski system string will always contain an 'A',
    # and the Sierpinski system is the only one that will generate 'A's.
    elif 'A' in string:
        system = systems.sierpinski
        # The turns for Sierpinski are set to 30 degrees each direction
        leftTurn = (1/3)*m.pi
        rightTurn = (-1/3)*m.pi
        scale_factor = 1/2
        # The number of variables each variable expands to is 3 for both variables
        vars_factor = 3
    # The only other predefined system is the Koch curve
    else:
        system = systems.koch
        # The turns for Koch are set to 30 degrees left and 60 degrees right
        leftTurn = (1/3)*m.pi
        rightTurn = (-2/3)*m.pi
        scale_factor = 1/3
        vars_factor = 4
    # Unpack the system into appropriate parts
    consts, _, rules, segment_symbols = system
    if customSystem is None:
        # Variables are the left hand side of the dictionary of the system
        variables = list(rules.keys())
        # Count the total number of variables in the string
        num_vars = sum(string.count(v) for v in variables)
        # After i iterations,
        # num_vars = vars_factor**i
        i = m.log(num_vars, vars_factor)
        scale = scale_factor**i
    # A custom system won't be scaled
    else:
        scale = 1
    # Make an empty list to be filled with lengths and angles
    values = []
    # Translate the string to pairs of line_lengths and angles
    for c in string:
        # Add a length of line every time one of the segment symbols is encountered
        line_length = scale if c in segment_symbols else 0
        # Translate all L's to leftTurns and R's to rightTurns of no length
        if c == 'L':
            angle = leftTurn
        elif c == 'R':
            angle = rightTurn
        else:
            angle = 0
        # Add them pairwise to the list of values
        # Potentially slow,
        # could be sped up if necessary
        # by pre-allocating a list of the proper length
        values.append(line_length)
        values.append(angle)
    return values

# Takes a list of the format turtleGraph creates
# and plots it, generating the coordinates
# for the ends of the line segments along the way.
# Can optionally include the name of the L-system in the plot title,
# if given.
# Inputs: a list of line lengths followed by their turn angles;
# optionally the name of the L-system the curve was generated from.
# Outputs: none, but shows a plot.
def turtlePlot(turtleCommands, name=None):
    # Splits up the line lengths and turn angles
    # Every second value starting from the zeroth
    # resp. first is a line length resp. turn angle.
    steps = turtleCommands[::2]
    angles = turtleCommands[1::2]
    # Extra value inserted due to range in for loop
    # The argument order of np.insert is (vector, index, value)
    angles = np.insert(angles, 0, 0)
    steps = np.insert(steps, 0, 0)

    # Same number of values as number of angles
    dvalues = [None for _ in angles]
    xvalues = [None for _ in angles]

    # Initial values
    dvalues[0]=(np.array([1,0]))
    xvalues[0]=(np.array([0,0]))

    # Start looping from 1,
    # as the initial value is already defined
    for i in range(1,len(angles)):
        dvalues[i] = np.dot(np.array([[ m.cos(angles[i]), -m.sin(angles[i])],
               [m.sin(angles[i]), m.cos(angles[i])]]),dvalues[i-1])
        xvalues[i] = xvalues[i-1]+steps[i]*dvalues[i]
    # Unpacks vector of (x,y) coordinates into tuple of lists of x and y values
    # which is then unpacked so plt.plot(list of x-values, list of y-values)
    # is eventually called
    plt.plot(*zip(*xvalues))
    if name is None:
        plt.title("Your plot of choice")
    else:
        plt.title(name)
    plt.show()
