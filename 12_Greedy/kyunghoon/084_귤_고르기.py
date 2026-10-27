from collections import Counter


def solution(k, tangerine):
    ans = 0
    for cnt in sorted(Counter(tangerine).values(), reverse=True):
        k -= cnt
        ans += 1
        if k <= 0:
            break

    return ans
