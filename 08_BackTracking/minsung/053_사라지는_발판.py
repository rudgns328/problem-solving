def solution(board, aloc, bloc):
    row, col = len(board), len(board[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    def dfs(ar, ac, br, bc, turn):
        if turn == 0:
            r, c = ar, ac
        else:
            r, c = br, bc

        moves = []
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == 1:
                moves.append((nr, nc))

        if not moves:
            return False, 0

        win_steps = []
        lose_steps = []

        for nr, nc in moves:
            board[r][c] = 0

            if turn == 0 and br == r and bc == c:
                win_steps.append(1)
                board[r][c] = 1
                continue
            elif turn == 1 and ar == r and ac == c:
                win_steps.append(1)
                board[r][c] = 1
                continue

            if turn == 0:
                opponent_win, steps = dfs(nr, nc, br, bc, 1)
            else:
                opponent_win, steps = dfs(ar, ac, nr, nc, 0)

            board[r][c] = 1

            if opponent_win:
                lose_steps.append(steps + 1)
            else:
                win_steps.append(steps + 1)

        if win_steps:
            return True, min(win_steps)
        else:
            return False, max(lose_steps)

    win, result = dfs(aloc[0], aloc[1], bloc[0], bloc[1], 0)
    return result
