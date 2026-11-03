def solution(board):
    dp = [r[:] for r in board]
    row = len(board)
    col = len(board[0])

    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    answer = max(max(r) for r in dp)

    return answer * answer
