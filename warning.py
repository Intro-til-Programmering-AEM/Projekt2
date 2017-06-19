#Warning
import math as m

def shouldWarn(system,N):
    variables, constants, rules, initialString = system
    num_vars = [sum(string.count(v) for v in variables) for string in rules.values()]
    var_maks=max(num_vars)
    return N > m.log(7000,var_maks) #For bad computer

