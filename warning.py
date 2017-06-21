import math as m
from systems import max_vars

# A function that returns True if the length of the string is at risk of
# exceeding a predefined, empirically determined threshold
# (roughly as long as we were willing to wait for our slowest computer to run)
def shouldWarn(system,N):
    # The largest value the program advises the user to compute
    threshold = 2**18
    bound = max_vars(system)
    # If no variables expand to a string containing multiple variables,
    # the string size won't grow exponentially,
    # and taking the logarithm doesn't make sense mathematically.
    if bound <= 1:
        return N > threshold
    else:
        return N > m.log(threshold,bound)

