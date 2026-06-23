def solution(n, results):
    answer = 0
    win = [[False] * (n + 1) for _ in range(n + 1)]

    for a, b in results:
        win[a][b] = True

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if win[i][k] and win[k][j]:
                    win[i][j] = True

    for i in range(1, n + 1):
        count = sum(win[i][j] or win[j][i] for j in range(1, n + 1) if i != j)
        if count == n - 1:
            answer += 1

    return answer
