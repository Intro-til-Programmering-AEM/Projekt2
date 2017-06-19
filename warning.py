#Warning
import math as m

# A function that returns True if the string is at risk of exceeding some
# preset threshold
def shouldWarn(system,N):
    # The largest value the program advises the user to compute
    threshold = 7000
    # Unpack the system for easy access to each tuple
    variables, constants, rules, initialString = system
    # Make a list of occurences of variables produced by each variable when taking one step
    num_vars = [sum(string.count(v) for v in variables) for string in rules.values()]
    # Finds the highest
    var_maks=max(num_vars)
    return N > m.log(threshold,var_maks) #For bad computer

