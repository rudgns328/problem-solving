def solution(tickets):
    answer = ["ICN"]
    tickets.sort()
    visited = [False] * len(tickets)
        
    def dfs(start):
        if len(answer) == len(tickets) + 1:
            return True
        
        for i, (f, t) in enumerate(tickets):
            if f == start and not visited[i]:
                visited[i] = True
                answer.append(t)

                if dfs(t):
                    return True

                visited[i] = False
                answer.pop()
        
    dfs("ICN")
    return answer