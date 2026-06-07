def solution(n, times):
    left = min(times)
    right = n * max(times)
    mid = 0

    while left != right:
        mid = (left + right) // 2
        count = 0
        for t in times:
            count += mid // t
        if count >= n:
            right = mid
        else:
            left = mid + 1

    return right
