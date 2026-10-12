def solution(board):
    rows, cols = len(board), len(board[0])

    for i in range(1, rows):
        for j in range(1, cols):
            if board[i][j] != 0:
                board[i][j] = (
                    min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
                )

    max_num = max(max(row) for row in board)

    return max_num * max_num
