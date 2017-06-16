import numpy as np
import math as m
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
    d=np.zeros(2)
    # Takes every second value starting from the second
    angles=turtleCommands[1::2]
    steps=turtleCommands[::2]

    for i in range(1):
        d=np.dot(np.array([[ m.cos(angles[i]), -m.sin(angles[i])],
                  [ m.sin(angles[i]), m.cos(angles[i])]]),d)
        print(d)

