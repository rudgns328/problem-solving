from collections import deque
from collections import Counter


def solution(want, number, discount):
    w = dict(zip(want, number))
    discount = deque(discount)
    result = 0
    d = Counter(list(discount)[0:10])

    while len(discount) >= 10:
        d = Counter(list(discount)[0:10])

        if w.keys() <= d.keys():
            for k in w:
                if w[k] <= d[k]:
                    continue
                else:
                    discount.popleft()
                    break
            else:
                result += 1
                discount.popleft()
        else:
            discount.popleft()

    return result
