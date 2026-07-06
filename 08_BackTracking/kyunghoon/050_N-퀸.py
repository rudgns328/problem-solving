def solution(n):
    queen = set()
    answer = 0

    def check(row, col):
        for r, c in queen:
            if c == col or abs(r - row) == abs(c - col):
                return True
        return False

    def dfs(row, col):
        queen.add((row, col))

        if row == n - 1:
            queen.remove((row, col))
            return 1

        count = 0
        for i in range(n):
            if not check(row + 1, i):
                count += dfs(row + 1, i)

        queen.remove((row, col))
        return count

    for i in range(n):
        answer += dfs(0, i)

    return answer