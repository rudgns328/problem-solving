from collections import deque


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                s = (i, j)
            elif maps[i][j] == "L":
                l = (i, j)
            elif maps[i][j] == "E":
                e = (i, j)

    def bfs(s, e):
        queue = deque()
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]

        queue.append((s[0], s[1], 0))
        visited[s[0]][s[1]] = True

        while queue:
            x, y, dist = queue.popleft()

            if (x, y) == e:
                return dist

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if maps[nx][ny] != "X" and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))

        return -1

    s_to_l = bfs(s, l)
    l_to_e = bfs(l, e)

    if s_to_l == -1 or l_to_e == -1:
        return -1

    return s_to_l + l_to_e
