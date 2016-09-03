import math

def nth_lexicographic_permutation(digits, n):
    digits.sort()
    size = len(digits)

    if size == 1:
        return digits[0]

    sub_perms = math.factorial(size-1)
    idx = n // sub_perms
    first_digit = digits[idx]
    digits.remove(first_digit)

    return first_digit * 10 ** (size-1) + nth_lexicographic_permutation(digits, n - idx * sub_perms)

def run():
    return nth_lexicographic_permutation(
        [n for n in range(10)],
        999999
    )
