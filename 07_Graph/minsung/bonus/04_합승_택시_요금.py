import heapq
from collections import defaultdict

INF = 999999999


def solution(n, s, a, b, fares):
    answer = INF
    graph = defaultdict(list)

    for a_home, b_home, c in fares:
        graph[a_home].append((b_home, c))
        graph[b_home].append((a_home, c))

    def dijkstra(start):
        distances = [INF] * (n + 1)
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            cost, node = heapq.heappop(queue)
            if cost > distances[node]:
                continue
            for next_node, next_cost in graph[node]:
                new_cost = cost + next_cost
                if new_cost < distances[next_node]:
                    distances[next_node] = new_cost
                    heapq.heappush(queue, (new_cost, next_node))
        return distances

    dist_s = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)

    for k in range(1, n + 1):
        answer = min(answer, dist_s[k] + dist_a[k] + dist_b[k])

    return answer
