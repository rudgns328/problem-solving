from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    distance = [[-1] * m for _ in range(n)]

    def bfs(start):
        queue = deque([start])
        distance[0][0] = 1

        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            here = queue.popleft()
            x, y = here

            for dx, dy in direct:
                nx = x + dx
                ny = y + dy

                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and maps[nx][ny] == 1
                    and distance[nx][ny] == -1
                ):
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

        return distance[n - 1][m - 1]

    return bfs((0, 0))
