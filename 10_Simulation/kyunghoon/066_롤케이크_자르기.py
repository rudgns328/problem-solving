from collections import Counter

def solution(topping):
    answer = 0
    older = set()
    younger = Counter(topping)

    for t in topping:
        younger[t] -= 1
        older.add(t)
        
        if younger[t] == 0:
            del younger[t]
        if len(older) == len(younger):
            answer += 1

    return answer
