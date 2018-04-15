def decimal_expansion(d):
    e = 0
    mods = []
    while True:
        mod = (10 ** e) % d

        if mod == 0:
            return (len(mods), 0)
        elif mod in mods:
            s = mods.index(mod)
            return (s, len(mods) - s)
        else:
            mods.append(mod)
            e += 1


def recurring_cycle(d):
    return decimal_expansion(d)[1]
