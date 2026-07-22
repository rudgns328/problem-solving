def solution(n):
    width = [False] * n
    diagonal1 = [False] * (2 * n)
    diagonal2 = [False] * (2 * n)

    answer = [0]

    def backtrack(row):
        if row == n:
            answer[0] += 1
            return

        for col in range(n):
            if (
                not width[col]
                and not diagonal1[row + col]
                and not diagonal2[row - col + n]
            ):
                width[col] = True
                diagonal1[row + col] = True
                diagonal2[row - col + n] = True

                backtrack(row + 1)

                width[col] = False
                diagonal1[row + col] = False
                diagonal2[row - col + n] = False

    backtrack(0)
    return answer[0]
