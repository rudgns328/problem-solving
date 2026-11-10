from collections import deque

def solution(priorities, location):
    dq = deque((p, i) for i, p in enumerate(priorities))
    count = 0
    
    while dq:
        p, i = dq.popleft()
        if any(p < q for q, _ in dq):
            dq.append((p, i))
        else:
            count += 1
            if i == location:
                return count