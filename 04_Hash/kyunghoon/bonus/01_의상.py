from collections import Counter


def solution(clothes):
    answer = 1
    closet = Counter(c[1] for c in clothes)

    for v in closet.values():
        answer *= v + 1

    return answer - 1
