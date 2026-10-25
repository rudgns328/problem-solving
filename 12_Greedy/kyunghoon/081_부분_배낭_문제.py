def solution(items, weight_limit):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    ans = 0
    for w, v in items:
        if weight_limit <= 0:
            break
        if w <= weight_limit:
            ans += v
            weight_limit -= w
        else:
            ans += v * weight_limit / w
            break

    return ans
