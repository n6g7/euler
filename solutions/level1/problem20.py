import math
from tools.digits import sum_digits

def factorial_digit_sum(n):
    return sum_digits(math.factorial(n))

def run():
    return factorial_digit_sum(100)
