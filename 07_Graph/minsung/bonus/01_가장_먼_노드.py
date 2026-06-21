from collections import defaultdict, deque


def bfs(start, graph, n):
    distances = [-1] * (n + 1)
    distances[1] = 0
    queue = deque([1])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return distances


def solution(n, edge):
    graph = defaultdict(list)

    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    distances = bfs(1, graph, n)
    max_dist = max(distances[1:])

    return distances[1:].count(max_dist)
