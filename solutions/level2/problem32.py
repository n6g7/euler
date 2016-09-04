import math
from tools.digits import get_digits

def different_digits(*args, **kwargs):
    digits = set(range(1, 10))
    for n in args:
        for d in get_digits(n):
            if d not in digits or d == 0:
                return False
            digits.remove(d)
    return len(digits) == 0 if 'all' in kwargs and kwargs['all'] else True

def pandigital_products():
    digits = 9
    solutions = set()

    # We know c >= a:
    max_a = 10 ** (digits // 2)

    for a in range(1, max_a):
        if not different_digits(a):
            continue

        digits_a = math.floor(math.log10(a))+1
        max_b = 10 ** (9-2*digits_a)

        for b in range(1, min(a, max_b)):
            if not different_digits(a, b):
                continue

            c = a * b
            if different_digits(a, b, c, all=True):
                solutions.add(c)

    return sum(solutions)

def run():
    return pandigital_products()
