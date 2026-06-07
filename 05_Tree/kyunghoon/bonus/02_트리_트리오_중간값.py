from collections import deque, defaultdict


def bfs(start, graph, n):
    visited = [-1] * (n + 1)
    queue = deque()

    queue.append(start)
    visited[start] = 0

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)

    return visited


def solution(n, edges):
    answer = 0
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    dist1 = bfs(1, graph, n)
    u = dist1.index(max(dist1[1:]))

    dist2 = bfs(u, graph, n)
    v = dist2.index(max(dist2[1:]))

    dist3 = bfs(v, graph, n)

    max_from_u = max(dist2[i] for i in range(1, n + 1) if i != v)
    max_from_v = max(dist3[i] for i in range(1, n + 1) if i != u)

    answer = max(max_from_u, max_from_v)

    return answer
