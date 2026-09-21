def rob(houses):
    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    
    for i in range(2, len(houses)):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    return dp[-1]

def solution(money):
    case_a = rob(money[:-1])
    case_b = rob(money[1:])

    return max(case_a, case_b)