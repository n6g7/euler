def coin_sums(sum, coins):
    cache = {}

    def combinations(target, max_coin):
        if (target, max_coin) not in cache:
            if target == 0:
                return 1

            options = 0

            available_coins = [c for c in coins if c <= max_coin]

            for coin in available_coins:
                if coin <= target:
                    options += combinations(target-coin, coin)

            cache[(target, max_coin)] = options

        return cache[(target, max_coin)]

    return combinations(sum, max(coins))


def run():
    return coin_sums(200, [1, 2, 5, 10, 20, 50, 100, 200])
