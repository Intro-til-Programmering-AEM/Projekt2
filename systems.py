# Iterates an L-system once, without checking whether the symbols are legal.
# Inputs: a tuple `system` (variable symbols, constant symbol, variable replacement rules, initial string),
# which represents the the L-system;
# a string of valid symbols to perform the iteration over.
# Output: a string `string` of valid symbols resulting from the iteration
# Assumptions: `string` contains only legal symbols.
def step_unsafe(system, string):
    # Unpacks needed parts of tuple
    _, consts, dict, _ = system
    # Maps every symbol to a string
    # Constant symbols are mapped to a string containing themself
    # Variable symbols are mapped according to the replacement rules of the L-system
    # Joins all resulting strings into a single string of symbols, and returns it
    replaced = map(lambda s: str(s) if s in consts else dict[s], string)
    return "".join(replaced)

# Iterates an L-system once.
# Inputs: a tuple representing the L-system; a string of (possibly invalid) symbols.
# Output: A string of valid symbols.
# Errors: Throws AssertionError if not all symbols in the input string are valid.
def step(system, string):
    # Unpacks tuple
    vars, consts, _, _ = system
    # Concatenates the two lists to form a list of all valid symbols
    symbols = vars + consts
    if not all(c in symbols for c in string):
        raise AssertionError("Lindenmayer string contains illegal symbols")
    return step_unsafe(system, string)

koch_dict = {
    'S': "SLSRSLS",
}

koch = (['S'], ['L','R'], koch_dict, "S")

sierpinski_dict = {
    'A': "BRARB",
    'B': "ALBLA",
}

sierpinski = (['A','B'], ['L','R'], sierpinski_dict, "A")

names = {
    "Koch": koch,
    "Sierpinski": sierpinski
}

# Iterates an L-system N times from the initial string
# Inputs: a string `System` naming the L-system to be iterated;
# a non-negative integer `N`, the number of iterations to be performed.
# Output: a string of valid symbols.
# Assumptions: `System` is a key of `names`,
# `N` is a non-negative integer
# (iterating 0 times returns the initial string)
def LindIter(System, N):
    # Look up tuple of system description based on input string
    system = names[System]
    # last tuple element is the initial string
    string = system[3]
    # Repeatedly iterate
    for _ in range(N):
        string = step_unsafe(system, string)
    return string
