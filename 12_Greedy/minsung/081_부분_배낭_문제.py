def solution(items, weight_limit):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0

    for weight, value in items:
        if weight_limit >= weight:
            weight_limit -= weight
            total_value += value
        else:
            total_value += value * (weight_limit / weight)
            break
    return total_value
