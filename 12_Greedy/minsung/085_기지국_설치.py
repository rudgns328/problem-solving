import math


def solution(N, stations, W):
    answer = 0
    prev = 1

    for s in stations:
        start = s - W
        if start > prev:
            gap = start - prev
            answer += math.ceil(gap / (2 * W + 1))
        prev = s + W + 1

    if prev <= N:
        answer += math.ceil((N - prev + 1) / (2 * W + 1))

    return answer
