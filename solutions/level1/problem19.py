def count_sundays(years):
    return round(12 * years / 7)


def run():
    return count_sundays(100)


if __name__ == '__main__':
    print(run())
