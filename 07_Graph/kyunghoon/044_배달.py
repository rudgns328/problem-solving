from collections import defaultdict
from heapq import heappush, heappop
from math import inf

def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [inf] * (N + 1)
    dist[1] = 0
    visited = [False] * (N + 1)
    priority_queue = [(0, 1)]
    
    while priority_queue:
        current_dist, current_node = heappop(priority_queue)
        
        if visited[current_node]:
            continue
        
        visited[current_node] = True
        
        for neighbor, weight in graph[current_node]:
            new_distance = current_dist + weight
            if dist[neighbor] > new_distance:
                dist[neighbor] = new_distance
                heappush(priority_queue, (new_distance, neighbor))
                
    for i in dist:
        if i <= K:
            answer += 1
    
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))