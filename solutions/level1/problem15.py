cache = {}


def lattice_paths(n, m):
    a = min(n, m)
    b = max(n, m)

    if a == 1:
        return b+1

    if a not in cache or b not in cache[n]:
        if a not in cache:
            cache[a] = {}
        cache[a][b] = lattice_paths(a-1, b) + lattice_paths(a, b-1)

    return cache[a][b]


def run():
    return lattice_paths(20, 20)
