from collections import deque


def solution(progresses, speeds):
    answer = []
    queue = deque()

    for i in range(len(progresses)):
        n = 100 - progresses[i]
        if n % speeds[i] == 0:
            queue.append(n // speeds[i])
        else:
            queue.append(n // speeds[i] + 1)

    while queue:
        count = 1
        front = queue.popleft()

        while queue and queue[0] <= front:
            queue.popleft()
            count += 1

        answer.append(count)

    return answer
