def solution(keyinput, board):
    pos_x = board[0]
    pos_y = board[1]
    a, b = 0, 0
    if pos_x % 2 == 0:
        half_x = pos_x // 2
    else:
        half_x = (pos_x - 1) // 2
        
    if pos_y % 2 == 0:
        half_y = pos_y // 2
    else:
        half_y = (pos_y - 1) // 2
        
    def range_check(x, y):
        return -half_x <= x <= half_x and -half_y <= y <= half_y
    
    for key in keyinput:
        if key == "left":
            if range_check(a - 1, b):
                a -= 1
        if key == "right":
            if range_check(a + 1, b):
                a += 1
        if key == "up":
            if range_check(a, b + 1):
                b += 1
        if key == "down":
            if range_check(a, b - 1):
                b -= 1
    
    return [a, b]