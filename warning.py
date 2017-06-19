#Warning
import math as m

def shouldWarn(system,N):
    return N > m.log(7000,max_vars(system)) #For bad computer

def max_vars(system):
    variables, constants, rules, initialString = system
    num_vars = [sum(string.count(v) for v in variables) for string in rules.values()]
    return max(num_vars)