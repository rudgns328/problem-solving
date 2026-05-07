def solution(dirs):
    x, y = 0, 0
    answer = set()
    
    for i in dirs:
        if i == 'U':
            nx, ny = x, y+1
        elif i == 'D':
            nx, ny = x, y-1
        elif i == 'L':
            nx, ny = x-1, y
        elif i == 'R':
            nx, ny = x+1, y
            
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x, y = nx, ny
    
    return len(answer)//2