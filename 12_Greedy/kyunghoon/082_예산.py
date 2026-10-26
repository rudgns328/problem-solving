def solution(d, budget):
    answer = 0
    d.sort()
    for n in d:
        if n <= budget:
            budget -= n
            answer += 1
        else:
            break

    return answer
