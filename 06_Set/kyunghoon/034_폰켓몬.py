def solution(nums):
    answer = 0

    kind = set(nums)

    if len(nums) / 2 < len(kind):
        answer = len(nums) / 2
    else:
        answer = len(kind)

    return answer
