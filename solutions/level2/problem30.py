import math
from tools.digits import sum_digits

def digit_power(n):
    sum_digits_max = 9 ** n * (n+1)

    return sum([i for i in range(2, sum_digits_max+1) if sum_digits(i,n) == i])

def run():
    return digit_power(5)
