from solutions.level1.problem4 import is_palindrome


def is_bin_palindrome(n):
    b = bin(n)[2:]
    return is_palindrome(b)


def double_base_palindromes(max):
    return sum([
        n
        for n in range(max)
        if is_palindrome(n) and is_bin_palindrome(n)
    ])


def run():
    return double_base_palindromes(1000000)
