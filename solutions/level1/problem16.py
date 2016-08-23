import math

def power_digit_sum(n):
    p = 2 ** n

    s = 0
    for i in str(p):
        s += int(i)
    return s

if __name__ == '__main__':
    print(power_digit_sum(1000))
