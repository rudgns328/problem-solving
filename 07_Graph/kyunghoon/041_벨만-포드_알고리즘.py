from math import inf

def solution(num_vertices, edges, source):
    dist = [inf for _ in range(num_vertices)]
    dist[source] = 0
    
    for _ in range(num_vertices - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return -1
            
    return dist