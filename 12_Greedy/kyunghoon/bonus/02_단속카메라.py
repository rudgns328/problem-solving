def solution(routes):
    answer = 1
    routes.sort(key=lambda r: r[1])
    camera = routes[0][1]
    
    for s, e in routes:
        if s > camera:
            camera = e
            answer += 1
    
    return answer