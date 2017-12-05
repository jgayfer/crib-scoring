from itertools import chain


def powerset(s):
    """Compute and return the powerset of the given set"""
    pset = []
    x = len(s)
    for i in range(1 << x):
        pset.append([s[j] for j in range(x) if (i & (1 << j))])
    return pset
