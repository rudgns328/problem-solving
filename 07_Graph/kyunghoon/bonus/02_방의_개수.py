def solution(arrows):
    answer = 0
    visited = {(0, 0)}
    visited_edge = set() 
    start = (0, 0)
    dr = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1)
    ]
    
    for i in range(len(arrows)):
        x, y = dr[arrows[i]]
        nx = start[0] + x
        ny = start[1] + y
        edge = tuple(sorted([start, (nx, ny)]))
        if edge[1][1] > edge[0][1]:
            cross_edge = tuple(sorted([(edge[0][0], edge[0][1] + 1), (edge[1][0], edge[1][1] - 1)]))
        else:
            cross_edge = tuple(sorted([(edge[0][0], edge[0][1] - 1), (edge[1][0], edge[1][1] + 1)]))
            
        if (nx, ny) in visited and edge not in visited_edge:
            answer += 1
        if arrows[i] % 2 == 1 and cross_edge in visited_edge and edge not in visited_edge:
            answer += 1
        
        visited.add((nx, ny))
        visited_edge.add(edge)
        start = (nx, ny)
    
    return answer