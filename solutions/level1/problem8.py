from os import path

with open(path.abspath('solutions/level1/p008_number.txt'), 'r') as f:
    the_number = f.read()[:-1]


def greatest_product(digits_length):
    length = len(the_number)
    result = None

    for start in range(0, length-digits_length+1):
        digits = the_number[start:start+digits_length]

        m = 1
        for digit in digits:
            m *= int(digit)

        if result is None:
            result = m
        else:
            result = max(m, result)

    return result


def run():
    return greatest_product(13)
