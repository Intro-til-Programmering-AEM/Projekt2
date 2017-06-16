import numpy as np
import math as m
turtleCommands=np.array([1,0.5,1.5,0.2,1])

def turtlePlot(turtleCommands):
    x=np.array([0,0])
    # Takes every second value starting from the second
    angles=turtleCommands[1::2]
    steps=turtleCommands[::2]
    dvalues = [0 for _ in angles]
    dvalues[0]=(np.array([1,0]))
    xvalues = [0 for _ in angles]
    xvalues[0]=(np.array([0,0]))
    for i in range(1,len(angles)):
        dvalues[i] = np.dot(np.array([[ m.cos(angles[i]), -m.sin(angles[i])],
               [m.sin(angles[i]), m.cos(angles[i])]]),dvalues[i-1])
        xvalues[i] = xvalues[i-1]+steps[i]*dvalues[i]
    print(dvalues)
    print(xvalues)




