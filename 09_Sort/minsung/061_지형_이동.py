from collections import deque


def solution(land, height):
    answer = 0
    n = len(land)
    group = [[-1] * n for _ in range(n)]

    def bfs(r, c, group_id):
        queue = deque([(r, c)])
        group[r][c] = group_id
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and group[nx][ny] == -1:
                    if abs(land[nx][ny] - land[x][y]) <= height:
                        group[nx][ny] = group_id
                        queue.append((nx, ny))

    group_id = 0
    for r in range(n):
        for c in range(n):
            if group[r][c] == -1:
                bfs(r, c, group_id)
                group_id += 1

    edges = []
    for r in range(n):
        for c in range(n):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = r + dx, c + dy
                if 0 <= nx < n and 0 <= ny < n and group[r][c] != group[nx][ny]:
                    cost = abs(land[nx][ny] - land[r][c])
                    edges.append((cost, group[r][c], group[nx][ny]))

    edges.sort()
    parent = list(range(group_id))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    for cost, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            answer += cost

    return answer
