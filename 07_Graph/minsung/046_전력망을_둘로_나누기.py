import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

def dfs(node, graph, visited):
    visited.add(node)
    count = 1
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            count += dfs(neighbor, graph, visited)
    return count

def solution(n, wires):
    answer = n
    
    for i in range(len(wires)):
        graph = defaultdict(list)
        
        for j, (v1, v2) in enumerate(wires):
            if j == i:
                continue
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        count = dfs(1, graph, set())
        
        diff = abs(count - (n - count))
        answer = min(answer, diff)
        
    return answer