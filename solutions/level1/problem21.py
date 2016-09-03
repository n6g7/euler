from tools.divisors import sum_divisors

def get_amicables(max):
    amicables = []

    for i in range(1, max+1):
        if i in amicables:
            continue

        d = sum_divisors(i, proper=True)

        if d > i:
            j = sum_divisors(d, proper=True)
            if j == i:
                amicables.append(i)
                amicables.append(d)
    return amicables

def sum_amicables(max):
    return sum(get_amicables(max))

def run():
    return sum_amicables(10000)
