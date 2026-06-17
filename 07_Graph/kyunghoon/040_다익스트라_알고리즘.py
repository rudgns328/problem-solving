from heapq import heappop, heappush
import math
from collections import defaultdict

def solution(start, numNodes, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        
    dist = [math.inf] * numNodes
    dist[start] = 0
    visited = [False] * numNodes
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, current_node = heappop(priority_queue)
        
        if visited[current_node] == True:
            continue
        
        visited[current_node] = True
        
        for neighbor, weight in graph[current_node]:
            new_distance = current_dist + weight
            if dist[neighbor] > new_distance:
                dist[neighbor] = new_distance
                heappush(priority_queue, (new_distance, neighbor))
                
    return dist