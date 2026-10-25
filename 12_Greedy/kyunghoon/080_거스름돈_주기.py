def solution(amount):
    change = []
    for coin in [100, 50, 10, 1]:
        if amount == 0:
            break
        count, amount = divmod(amount, coin)
        change.extend([coin] * count)
    return change