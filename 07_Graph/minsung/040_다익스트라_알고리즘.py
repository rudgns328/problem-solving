import heapq
from collections import defaultdict, deque

INF = 999999999


def solution(start, num_nodes, edges):
    graph = defaultdict(list)
    for from_node, to_node, weight in edges:
        graph[from_node].append((to_node, weight))

    distances = [INF] * num_nodes
    visited = [False] * num_nodes
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if visited(current_node):
            continue

        visited[current_node] = True

        for neighbor, weight in graph[current_node]:
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappop(priority_queue, (new_distance, neighbor))

    return distances
