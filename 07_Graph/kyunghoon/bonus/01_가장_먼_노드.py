from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    dist = [0] * (n + 1)
    
    def bfs(start):
        queue = deque([(start, 0)])
        visited = [False] * (n + 1)
        visited[start] = True
        while queue:
            node, distance = queue.popleft()
            dist[node] = distance
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, distance + 1))
                    
    bfs(1)
    
    max_dist = max(dist[1:])                
    result = [x for x in dist if x == max_dist]
        
    return len(result)