def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(node, visited):
        visited[node] = True
        cnt = 1
        for v in graph[node]:
            if not visited[v]:
                cnt += dfs(v, visited)
        return cnt
    
    answer = n
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        visited = [False] * (n + 1)
        cnt = dfs(a, visited)
        answer = min(answer, abs(2 * cnt - n))
        graph[a].append(b)
        graph[b].append(a)
        
    return answer