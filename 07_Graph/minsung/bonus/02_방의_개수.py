def solution(arrows):
    answer = 0
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    visited_node = set()
    visited_edge = set()

    x, y = 0, 0
    visited_node.add((x, y))

    for arrow in arrows:
        for _ in range(2):
            x += dx[arrow]
            y += dy[arrow]

            is_new_node = (x, y) not in visited_node
            is_new_edge = (x, y, x - dx[arrow], y - dy[arrow]) not in visited_edge

            if not is_new_node and is_new_edge:
                answer += 1

            visited_node.add((x, y))
            visited_edge.add((x, y, x - dx[arrow], y - dy[arrow]))
            visited_edge.add((x - dx[arrow], y - dy[arrow], x, y))

    return answer
