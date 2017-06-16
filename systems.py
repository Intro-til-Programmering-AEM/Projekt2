def step(system, string):
    vars, consts, dict, _ = system
    return "".join(map(lambda s: str(s) if s in consts else dict[s], string))

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

def LindIter(System, N):
    system = names[System]
    string = system[3]
    for _ in range(N):
        string = step(system, string)
    return string
