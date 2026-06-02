from collections import deque, defaultdict


def solution(n, edges):
    answer = 0
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[node] + 1
                    queue.append(nxt)
        return dist

    dist_from_1 = bfs(1)
    a = dist_from_1.index(max(dist_from_1[1:]), 1)

    dist_a = bfs(a)
    b = dist_a.index(max(dist_a[1:]), 1)

    dist_b = bfs(b)

    for c in range(1, n + 1):
        if c == a or c == b:
            continue
        answer = max(answer, dist_a[c], dist_b[c])

    return answer
