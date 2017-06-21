#Warning
import math as m

# A function that returns True if the length of the string is at risk of
# exceeding some predefined threshold
def shouldWarn(system,N):
    # The largest value the program advises the user to compute
    threshold = 2**18
    bound = max_vars(system)
    if bound <= 1:
        return N > threshold
    return N > m.log(threshold,bound)

# A function that returns the maximum number of variables a single variable can produce
# for a given system
def max_vars(system):
    # Unpack the system for easy access to each tuple
    constants, initialString, rules, _ = system
    variables = list(rules.keys())
    # Make a list of occurences of variables produced by each variable when taking one step
    num_vars = [sum(string.count(v) for v in variables) for string in rules.values()]
    # the highest number of occurences is returned if there are any
    if num_vars:
        return max(num_vars)
    else:
        return 0
