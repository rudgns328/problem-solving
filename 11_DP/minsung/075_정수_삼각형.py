def solution(triangle):
    dp = [row[:] for row in triangle]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i - 1][0]
            elif j == i:
                dp[i][j] = triangle[i][j] + dp[i - 1][i - 1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])

    return max(dp[-1])
