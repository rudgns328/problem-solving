def solution(board, moves):
    bucket = []
    result = 0
    while moves:
        n = moves.pop(0)
        for i in range(len(board)):
            if board[i][n - 1] == 0:
                continue
            else:
                bucket.append(board[i][n - 1])
                board[i][n - 1] = 0
                if len(bucket) > 1 and bucket[-1] == bucket[-2]:
                    bucket.pop()
                    bucket.pop()
                    result += 2
                break
    return result
