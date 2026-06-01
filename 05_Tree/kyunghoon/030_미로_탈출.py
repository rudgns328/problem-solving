from collections import deque


def solution(maps):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

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
            y, x, dist = queue.popleft()

            if (y, x) == e:
                return dist

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                    if maps[ny][nx] != "X" and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((ny, nx, dist + 1))

        return -1

    s_to_l = bfs(s, l)
    l_to_e = bfs(l, e)

    if s_to_l == -1 or l_to_e == -1:
        return -1

    return s_to_l + l_to_e
