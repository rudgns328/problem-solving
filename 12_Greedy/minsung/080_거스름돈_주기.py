def solution(amount):
    coins = [100, 50, 10, 1]
    change = []
    for coin in coins:
        count = amount // coin
        change += [coin] * count
        amount %= coin
    return change
