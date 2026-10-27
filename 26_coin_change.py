def coin_change(coins, amount):
    minimum = [amount + 1] * (amount + 1)
    minimum[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                minimum[value] = min(minimum[value], minimum[value - coin] + 1)

    return minimum[amount] if minimum[amount] <= amount else -1


assert coin_change([1, 2, 5], 11) == 3
assert coin_change([2], 3) == -1
