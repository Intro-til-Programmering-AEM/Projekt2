#Warning
import math as m
from systems import max_vars

# A function that returns True if the length of the string is at risk of
# exceeding some predefined threshold
def shouldWarn(system,N):
    # The largest value the program advises the user to compute
    threshold = 2**18
    bound = max_vars(system)
    if bound <= 1:
        return N > threshold
    return N > m.log(threshold,bound)

