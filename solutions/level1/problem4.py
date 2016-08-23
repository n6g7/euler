import math

def is_palindrome(n):
    s = str(n)
    return s[::-1] == s

def palindromes(max):
    for i in range(max, 1, -1):
        for j in range(max, i-1, -1):
            r = i*j
            if is_palindrome(r):
                yield r

def largest_palindrome_by_magnitude(n):
    return max([r for r in palindromes(10 ** n)])

if __name__ == '__main__':
    print(largest_palindrome_by_magnitude(3))
