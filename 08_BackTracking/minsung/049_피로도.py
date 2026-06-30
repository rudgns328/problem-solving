k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

def solution(k, dungeons):
    answer = [0]
    visited = [False] * len(dungeons)
    
    def backtrack(k, count):
        answer[0] = max(answer[0], count)
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                backtrack(k - dungeons[i][1], count + 1)
                visited[i] = False
        
    backtrack(k, 0)
    return answer[0]

print(solution(k, dungeons))