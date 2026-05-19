from collections import deque, Counter


def solution(want, number, discount):
    w = dict(zip(want, number))
    discount = deque(discount)
    result = 0

    d = Counter(list(discount)[0:10])

    while len(discount) >= 10:
        if w.keys() <= d.keys():
            for k in w:
                if w[k] <= d[k]:
                    continue
                else:
                    break
            else:
                result += 1

        out = discount.popleft()
        d[out] -= 1
        if d[out] == 0:
            del d[out]

        if len(discount) >= 10:
            d[discount[9]] += 1

    return result
