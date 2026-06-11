INF = 999999999


def solution(num_vertices, edges, source):
    graph = [[] for _ in range(num_vertices)]
    for edge in edges:
        from_vertex, to_vertex, weight = edge
        graph[from_vertex].append((to_vertex, weight))

    distances = [INF] * num_vertices
    distances[source] = 0

    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    for u in range(num_vertices):
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                return [-1]

    return distances
