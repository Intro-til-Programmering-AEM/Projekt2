import numpy as np
import math as m
turtleCommands=np.array([1,0.5,1.5,0.2,1])

def turtlePlot(turtleCommands):
    x=np.array([0,0])
    d=np.array([1,0])
    # Takes every second value starting from the second
    angles=turtleCommands[1::2]
    steps=turtleCommands[::2]
    for i in range(len(angles)):
        d=np.dot(np.array([[m.cos(angles[i]),-m.sin(angles[i])],
                            [m.sin(angles[i]),m.cos(angles[i])]]),d)
        print(d)
