def dp(houses):
    n = len(houses)
    dp = [0] * n

    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    return dp[n - 1]


def solution(money):
    result1 = dp(money[:-1])
    result2 = dp(money[1:])

    return max(result1, result2)
