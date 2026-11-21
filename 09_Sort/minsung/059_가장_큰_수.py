from functools import cmp_to_key


def solution(numbers):
    nums = list(map(str, numbers))

    compare = lambda a, b: -1 if a + b > b + a else (1 if a + b < b + a else 0)

    nums.sort(key=cmp_to_key(compare))
    answer = "".join(nums)

    return "0" if answer[0] == "0" else answer
