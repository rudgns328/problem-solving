def solution(arr):
    ans = []

    for a in arr:
        if a != ans[-1:]:
            ans.append(a)

    return ans
