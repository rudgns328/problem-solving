import heapq
from collections import defaultdict

INF = 999999999


def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for from_node, to_node, time in road:
        graph[from_node].append((to_node, time))
        graph[to_node].append((from_node, time))

    distances = [INF] * (N + 1)
    visited = [False] * (N + 1)
    distances[1] = 0

    priority_queue = [(0, 1)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue

        visited[current_node] = True

        for next_node, next_time in graph[current_node]:
            new_distance = distances[current_node] + next_time
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(priority_queue, (new_distance, next_node))

    for d in distances[1:]:
        if d <= K:
            answer += 1

    return answer
