from fractions import Fraction
from functools import reduce


def simplify(fn, fd):
    n = list(str(fn))
    d = list(str(fd))

    for x in n:
        if x in d:
            n.remove(x)
            d.remove(x)

    if len(n) == 0 or len(d) == 0:
        return (fn, fd)

    new_n = int(''.join(n))
    new_d = int(''.join(d))

    if new_d == 0:
        return (fn, fd)

    return (new_n, new_d)


def is_curious(fn, fd):
    if fd % 10 == 0 and fn % 10 == 0:
        return False

    (sn, sd) = simplify(fn, fd)
    return sd != fd and Fraction(fn, fd) == Fraction(sn, sd)


def curious_fractions(min, max_denominator):
    curious = []

    for d in range(min, max_denominator):
        for n in range(min, d):
            if is_curious(n, d):
                curious.append(Fraction(n, d))

    product = reduce(
        lambda acc, f: acc * f,
        curious
    )

    return product.denominator


def run():
    return curious_fractions(10, 100)
