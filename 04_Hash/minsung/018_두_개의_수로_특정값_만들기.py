def solution(arr, target):
    hash = [0] * (target + 1)

    for n in arr:
        if n <= target:
            hash[n] = 1

    for n in arr:
        if n >= target:
            continue
        if (target - n) == n:
            continue
        if hash[(target - n)]:
            return True

    return False
