from collections import defaultdict, deque

adj_list = defaultdict(list)
result = []

def bfs(node):
    queue = deque([node])
    visited = set()
    visited.add(node)
    result.append(node)
    
    while queue:
        current = queue.popleft()
        
        for n in adj_list[current]:
            if n not in visited:
                queue.append(n)
                visited.add(n)
                result.append(n)
    
def solution(graph, start):
    for k, v in graph:
        adj_list[k].append(v)
        
    bfs(start)
    
    return result