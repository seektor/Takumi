def flat_map(f, list):
    return [item for sublist in list for item in f(sublist)]
