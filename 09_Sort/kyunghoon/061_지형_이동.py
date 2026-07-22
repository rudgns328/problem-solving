import sys
sys.setrecursionlimit(100000)

def solution(land, height):
    n = len(land)
    visited = [[False] * n for _ in range(n)]
    group_of = [[-1] * n for _ in range(n)]
    group_id = 0
    
    def dfs(r, c, group_id):
        visited[r][c] = True
        group_of[r][c] = group_id
        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == False:
                if abs(land[nr][nc] - land[r][c]) <= height:
                    dfs(nr, nc, group_id)
    
    for r in range(n):
        for c in range(n):
            if visited[r][c] == False:
                dfs(r, c, group_id)
                group_id += 1
                
    edges = []
    
    for r in range(n):
        for c in range(n):
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    a = group_of[r][c]
                    b = group_of[nr][nc]
                    if a != b:
                        cost = abs(land[r][c] - land[nr][nc])
                        edges.append((cost, a, b))
    
    parent = [i for i in range(group_id)]
    edges.sort()
    total_cost = 0
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX != rootY:
            parent[rootX] = rootY
            return True
        return False
    
    for (cost, a, b) in edges:
        if union(a, b):
            total_cost += cost
        
    return total_cost