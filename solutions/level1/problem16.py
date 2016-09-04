from tools.digits import sum_digits

def power_digit_sum(n):
    return sum_digits(2 ** n)

def run():
    return power_digit_sum(1000)
