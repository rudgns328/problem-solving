from collections import defaultdict
import math

def solution(start, numNodes, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        
    nodes = list(range(numNodes))
    dist = {node: math.inf for node in nodes}
    dist[start] = 0
    prev = {node: None for node in nodes}
    visited = []
    
    while(len(visited) < numNodes):
        current = None
        for node in nodes:
            if node not in visited:
                if current is None or dist[node] < dist[current]:
                    current = node
        
        if dist[current] == math.inf:
            break
        
        visited.append(current)
        
        for v, w in graph[current]:
            new_w = dist[current] + w 
            if new_w < dist[v]:
                dist[v] = new_w
                prev[v] = current
                
    return list(dist.values())