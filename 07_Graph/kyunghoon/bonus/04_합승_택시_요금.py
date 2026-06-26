from heapq import heappush, heappop
from collections import defaultdict

INF = 10**9

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
    s_dist = [INF] * (n + 1)
    a_dist = [INF] * (n + 1)
    b_dist = [INF] * (n + 1)
    s_dist[s] = 0
    a_dist[a] = 0
    b_dist[b] = 0
    s_visited = [False] * (n + 1)
    a_visited = [False] * (n + 1)
    b_visited = [False] * (n + 1)
    s_priority_queue = [(0, s)]
    a_priority_queue = [(0, a)]
    b_priority_queue = [(0, b)]
    
    while s_priority_queue:
        current_dist, current_node = heappop(s_priority_queue)
        
        if s_visited[current_node]:
            continue
        
        s_visited[current_node] = True
        
        for neighbor, weight in graph[current_node]:
            new_distance = current_dist + weight
            
            if s_dist[neighbor] > new_distance:
                s_dist[neighbor] = new_distance
                heappush(s_priority_queue, (new_distance, neighbor))
                
    while a_priority_queue:
        current_dist, current_node = heappop(a_priority_queue)
        
        if a_visited[current_node]:
            continue
        
        a_visited[current_node] = True
        
        for neighbor, weight in graph[current_node]:
            new_distance = current_dist + weight
            
            if a_dist[neighbor] > new_distance:
                a_dist[neighbor] = new_distance
                heappush(a_priority_queue, (new_distance, neighbor))
                
    while b_priority_queue:
        current_dist, current_node = heappop(b_priority_queue)
        
        if b_visited[current_node]:
            continue
        
        b_visited[current_node] = True
        
        for neighbor, weight in graph[current_node]:
            new_distance = current_dist + weight
            
            if b_dist[neighbor] > new_distance:
                b_dist[neighbor] = new_distance
                heappush(b_priority_queue, (new_distance, neighbor))
    
    answer = min(s_dist[k] + a_dist[k] + b_dist[k] for k in range(1, n+1))
    
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))