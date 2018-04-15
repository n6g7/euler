from os import path


def alphabetical_value(x):
    return sum([c-64 for c in map(ord, x)])


def get_names():
    with open(path.abspath('solutions/level1/p022_names.txt'), 'r') as f:
        return [x.strip('"') for x in f.read().split(',')]


def names_scores():
    names = get_names()
    names.sort()

    total = 0

    for i, name in enumerate(names):
        total += (i+1) * alphabetical_value(name)

    return total


def run():
    return names_scores()
