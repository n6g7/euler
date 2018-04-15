import math

from tools.digits import get_digits


def is_curious(n):
    return sum([
        math.factorial(d)
        for d in get_digits(n)
    ]) == n


def digit_factorials(max):
    return sum([
        n
        for n in range(3, max)
        if is_curious(n)
    ])


def run():
    return digit_factorials(100000)
