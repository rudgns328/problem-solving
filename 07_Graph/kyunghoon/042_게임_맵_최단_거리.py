from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    end = (rows - 1, cols - 1)
    queue = deque()
    queue.append((0, 0, 1))
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    directions = [(-1, 0), (1, 0), (0,-1), (0, 1)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == end:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if maps[nr][nc] != 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))
                    
    return -1