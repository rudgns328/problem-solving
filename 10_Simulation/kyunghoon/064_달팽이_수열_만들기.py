def solution(n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    arr = [[0] * n for _ in range(n)]
    arr[0][0] = 1
    x, y = 0, 0
    d = 0
    
    def is_movable(nx, ny):
        return 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0
    
    for num in range(2, n * n + 1):
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if not is_movable(nx, ny):
            d = (d + 1) % 4
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
        arr[nx][ny] = num
        x, y = nx, ny

    return arr