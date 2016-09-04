from tools.fraction import recurring_cycle

def longest_recurring_cycle(limit):
    max_d = 0
    max_cycle = 0
    for d in range(1, limit+1):
        cycle = recurring_cycle(d)
        if cycle > max_cycle:
            (max_d, max_cycle) = (d, cycle)
    return max_d

def run():
    return longest_recurring_cycle(1000)
