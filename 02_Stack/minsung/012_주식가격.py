def solution(prices):
    n = len(prices)
    answer = [0] * n

    stack = [0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)

    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx

    return answer
