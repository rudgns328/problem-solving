from collections import deque


def solution(priorities, location):
    queue = deque((p, i) for i, p in enumerate(priorities))
    count = 0

    while queue:
        process = queue.popleft()

        if any(p > process[0] for p, i in queue):
            queue.append(process)
        else:
            count += 1
            if location == process[1]:
                return count
