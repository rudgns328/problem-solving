def solution(n, stations, w):
    answer = 0
    cover = 2 * w + 1
    start = 1

    for s in stations:
        l = s - w - start
        answer += (l + cover - 1) // cover
        start = s + w + 1

    answer += (n - start + 1 + cover - 1) // cover 
    return answer