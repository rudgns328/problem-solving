from collections import deque

def solution(people, limit):
    # 1. people 내림차순 정렬
    # 2. 앞에서부터 limit - 제일 작은 수 + 해당 원소 > limit 보다 크면 popleft()
    # 3. 아닐 시 break
    # 4. 남은 배열 길이 / 2 or 홀수면 /2 + 1 
    answer = 0
    people.sort(reverse=True)
    dq = deque(people)
    while dq:
        if len(dq) == 1:
            answer += 1
            break
        elif dq[0] + dq[-1] <= limit:
            answer += 1
            dq.popleft()
            dq.pop()
        else:
            answer += 1
            dq.popleft()
    return answer

print(solution([70, 80, 50], 100))