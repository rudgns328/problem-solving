def solution(keyinput, board):
    x, y = 0, 0
    max_x = board[0] // 2
    max_y = board[1] // 2

    move = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}

    for key in keyinput:
        dx, dy = move[key]
        nx, ny = x + dx, y + dy
        if -max_x <= nx <= max_x and -max_y <= ny <= max_y:
            x, y = nx, ny

    return [x, y]
