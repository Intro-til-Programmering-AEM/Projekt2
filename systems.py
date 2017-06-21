# Computer-friendly descriptions of the L-systems are defined in this module.
# These will be constants used throughout the program where access to
# a specific, predefined system is needed.
# Functions for working with them (e.g. iterating them) are also defined.

# A dictionary mapping symbols to strings
# as determined by the rules for the system.
koch_dict = {
    'S': "SLSRSLS",
}

# A tuple (constant symbols, initial string, variable replacement rules, symbols representing line segments),
# which contains information fully describing the system.
koch = (['L','R'], "S", koch_dict, ['S'])


sierpinski_dict = {
    'A': "BRARB",
    'B': "ALBLA",
}

sierpinski = (['L','R'], "A", sierpinski_dict, ['A', 'B'])

# A dictionary mapping the name of the system as given in the specification
# to the system tuple as defined in this module.
names = {
    "Koch": koch,
    "Sierpinski": sierpinski
}

# Iterates an L-system N times from its initial string
# Inputs: a string `System` naming the L-system to be iterated;
# a non-negative integer `N`, the number of iterations to be performed.
# Output: a string of valid symbols.
# Assumptions: `System` is a key of `names`,
# `N` is a non-negative integer
# (iterating 0 times returns the initial string)
def LindIter(System, N):
    # Look up tuple of system description based on input string
    system = names[System]
    # Then delegate the actual work to iterate
    return iterate(system, N)


# Iterates an L-system N times from its initial string
# Inputs: a tuple `system` describing the L-system to be iterated;
# a non-negative integer `N`, the number of iterations to be performed.
# Output: a string of valid symbols.
# Assumptions: `N` is a non-negative integer
# (iterating 0 times returns the initial string)
def iterate(system, N):
    # Second tuple element is the initial string
    string = system[1]
    for _ in range(N):
        string = step_unsafe(system, string)
    return string

# Iterates an L-system once, without checking whether the symbols are legal.
# Inputs: a tuple `system` which represents the the L-system;
# a string of valid symbols to perform the iteration over.
# Output: a string `string` of valid symbols resulting from the iteration.
# Assumptions: `string` contains only legal symbols.
def step_unsafe(system, string):
    # Unpacks needed parts of tuple
    consts, _, dict, _ = system
    # Maps every symbol to a string
    # Any constant symbol is mapped to a string containing itself
    # Variable symbols are mapped according to the replacement rules of the L-system
    replaced = map(lambda s: str(s) if s in consts else dict[s], string)
    # Joins all resulting strings into a single string of symbols, and returns it
    return "".join(replaced)

# Iterates an L-system once.
# Inputs: a tuple representing the L-system; a string of (possibly invalid) symbols.
# Output: A string of valid symbols.
# Errors: Throws AssertionError if not all symbols in the input string are valid.
# Not used in the program as we only step in conditions that have already been confirmed
# not to contain or generate illegal symbols,
# but included for completeness.
def step(system, string):
    # Unpacks tuple
    consts, _, rules, _ = system
    # The variables are the symbols that replacement rules exist for
    variables = list(rules.keys())
    # Concatenates the two lists to form a list of all valid symbols
    symbols = variables + consts
    if not all(c in symbols for c in string):
        raise AssertionError("Lindenmayer string contains illegal symbols")
    return step_unsafe(system, string)

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
