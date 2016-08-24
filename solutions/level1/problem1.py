def sum_multiples(max):
    multiples = set(range(0, max, 3)) | set(range(0, max, 5))

    return sum(multiples)

def run():
    return sum_multiples(1000)
