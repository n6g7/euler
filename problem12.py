from tools.divisors import count_divisors
from tools.sequence.triangle_numbers import triangle_numbers

def triangle_numbers_divisors(number_divisors):
    for n in triangle_numbers():
        if count_divisors(n) > number_divisors:
            return n

if __name__ == '__main__':
    print(triangle_numbers_divisors(500))
