def solution(board, aloc, bloc):
    N, M = len(board), len(board[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def in_range(y, x):
        return 0 <= y < N and 0 <= x < M

    def dfs(cur, opp):
        cy, cx = cur
        oy, ox = opp

        moves = []
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if in_range(ny, nx) and board[ny][nx] == 1:
                moves.append((ny, nx))

        if not moves:
            return (False, 0)

        best_win_moves = None
        best_lose_moves = None

        for ny, nx in moves:
            board[cy][cx] = 0

            if (oy, ox) == (cy, cx):
                result = (True, 1)
            else:
                opp_win, opp_moves = dfs(opp, (ny, nx))
                result = (not opp_win, opp_moves + 1)

            board[cy][cx] = 1

            win, cnt = result
            if win:
                if best_win_moves is None or cnt < best_win_moves:
                    best_win_moves = cnt
            else:
                if best_lose_moves is None or cnt > best_lose_moves:
                    best_lose_moves = cnt

        if best_win_moves is not None:
            return (True, best_win_moves)
        else:
            return (False, best_lose_moves)

    a_win, total_moves = dfs(tuple(aloc), tuple(bloc))
    return total_moves