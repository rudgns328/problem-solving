from collections import deque


def solution(progresses, speeds):
    answer = []
    day = deque()
    for i in range(len(progresses)):
        n = 100 - progresses[i]
        if n % speeds[i] == 0:
            day.append(n // speeds[i])
        else:
            day.append(n // speeds[i] + 1)
    i = 0
    count = 1
    while day:
        now = day[0]
        if len(day) == 1:
            answer.append(1)
            break
        if i + 1 == len(day):
            answer.append(count)
            break
        if now < day[i + 1]:
            answer.append(count)
            for _ in range(count):
                day.popleft()
            i = 0
            count = 1
        else:
            i += 1
            count += 1

    return answer
