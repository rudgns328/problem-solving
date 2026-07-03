def solution(k, dungeons):
    visited = [False] * len(dungeons)
    def dfs(k, count):
        best = count
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                best = max(best, dfs(k - dungeons[i][1], count + 1))
                visited[i] = False            
        return best
    
    return dfs(k, 0)