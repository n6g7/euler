from tools.digit_sum import digit_sum

def power_digit_sum(n):
    return digit_sum(2 ** n)

def run():
    return power_digit_sum(1000)
