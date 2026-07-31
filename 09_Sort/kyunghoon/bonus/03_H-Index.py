def solution(citations):
    answer = 0
    c = len(citations)
    for i in range(0, c + 1):
        count = sum(1 for x in citations if x >= i)
        if count >= i:
            answer = i
    
    return answer

