#Warning
import math as m

# A function that returns True if the string is at risk of exceeding some
# preset threshold
def shouldWarn(system,N):
    # The largest value the program advises the user to compute
    threshold = 7000
    bound = max_vars(system)
    if bound == 1:
        return False
    return N > m.log(threshold,bound) #For bad computer

# A function that returns an estimate of maximum
def max_vars(system):
    constants, initialString, rules, _ = system
    variables = list(rules.keys())
    # Make a list of occurences of variables produced by each variable when taking one step
    num_vars = [sum(string.count(v) for v in variables) for string in rules.values()]
    return max(num_vars)

