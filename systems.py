def step(system, string):
    vars, consts, dict, _ = system
    return "".join(map(lambda s: str(s) if s in consts else dict[s], string))
