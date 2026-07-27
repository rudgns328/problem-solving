def solution(n, info):
    best = [[-1]]
    ryan = [0] * 11
    answer = [-1]

    def calculate_score():
        return sum(
            (10 - i) * (1 if ryan[i] > a else -1)
            for i, a in enumerate(info)
            if ryan[i] or a
        )

    def is_better(cur, prev):
        return next(
            (cur[i] > prev[i] for i in range(10, -1, -1) if cur[i] != prev[i]), False
        )

    def dfs(index, left):
        if index == 11:
            ryan[10] += left
            diff = calculate_score()
            if diff > 0 and (
                diff > answer[0] or (diff == answer[0] and is_better(ryan, best[0]))
            ):
                answer[0] = diff
                best[0] = ryan[:]
            ryan[10] -= left
            return

        if left >= (need := info[index] + 1):
            ryan[index] = need
            dfs(index + 1, left - need)
            ryan[index] = 0

        dfs(index + 1, left)

    dfs(0, n)
    return best[0]
