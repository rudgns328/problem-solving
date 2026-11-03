def solution(strs, t):
    dp = [20001] * (len(t) + 1)
    dp[0] = 0

    strs_set = set(strs)

    for i in range(1, len(t) + 1):
        for l in range(1, 6):
            if i >= l and t[i - l : i] in strs_set:
                dp[i] = min(dp[i], dp[i - l] + 1)

    if dp[len(t)] == 20001:
        return -1
    return dp[len(t)]
