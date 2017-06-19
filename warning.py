#Warning
import math as m

# A function that returns True if the string is at risk of exceeding some
# preset threshold
def shouldWarn(system,N):
    # The largest value the program advises the user to compute
    threshold = 7000
    return N > m.log(threshold,max_vars(system)) #For bad computer

# A function that returns an estimate of maximum
def max_vars(system):
    variables, constants, rules, initialString = system
    # Make a list of occurences of variables produced by each variable when taking one step
    num_vars = [sum(string.count(v) for v in variables) for string in rules.values()]
    return max(num_vars)

