#Warning
import math as m

# A function that returns True if the length of the string is at risk of
# exceeding some predefined threshold
def shouldWarn(system,N):
    # The largest value the program advises the user to compute
    threshold = 7000 # 'Safe'/low threshold set for a bad computer
    # Chech with a boolean statement whether the string might be too long
    return N > m.log(threshold,max_vars(system))

# A function that returns the maximum number of variables a single variable can produce
# for a given system
def max_vars(system):
    # Unpack the system for easy access to each tuple
    variables, constants, rules, initialString = system
    # Make a list of occurences of variables produced by each variable when taking one step
    num_vars = [sum(string.count(v) for v in variables) for string in rules.values()]
    # the highest number of occurences is returned
    return max(num_vars)
