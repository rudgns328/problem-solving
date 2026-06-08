def solution(nums):
    n = set(nums)
    k = len(nums) / 2
    if k < len(n):
        return k
    else:
        return len(n)
