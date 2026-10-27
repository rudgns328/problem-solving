from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    dq = deque(people)
    
    while dq:
        if len(dq) >= 2 and dq[0] + dq[-1] <= limit:
            dq.pop()
        dq.popleft()
        answer += 1
        
    return answer