import math
from tools.digit_sum import digit_sum

def factorial_digit_sum(n):
    return digit_sum(math.factorial(n))

def run():
    return factorial_digit_sum(100)
