def solution(arr, target):
    filtered = [num for num in arr if num < target]

    hash = [0] * (target + 1)

    for num in filtered:
        hash[num] = 1

    for num in filtered:
        if (target - num) == num:
            continue
        if hash[target - num]:
            return True

    return False
