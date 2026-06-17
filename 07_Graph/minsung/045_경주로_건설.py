import heapq

INF = 999999999


def solution(board):
    n = len(board)
    distances = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    priority_queue = []

    for d in range(4):
        distances[0][0][d] = 0
        heapq.heappush(priority_queue, (0, 0, 0, d))

    while priority_queue:
        current_cost, x, y, current_direction = heapq.heappop(priority_queue)

        if current_cost > distances[x][y][current_direction]:
            continue

        for d, (dx, dy) in enumerate(directions):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:

                if d == current_direction:
                    new_cost = current_cost + 100
                else:
                    new_cost = current_cost + 600

                if new_cost < distances[nx][ny][d]:
                    distances[nx][ny][d] = new_cost
                    heapq.heappush(priority_queue, (new_cost, nx, ny, d))

    return min(distances[n - 1][n - 1])
