def solution(strs, t):
    n = len(t)
    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[0] = 0
    pieces = set(strs)

    for i in range(1, n + 1):
        for L in range(1, 6):
            if i - L < 0:
                continue
            if t[i - L : i] in pieces:
                dp[i] = min(dp[i - L] + 1, dp[i])

    return dp[n] if dp[n] < INF else -1
