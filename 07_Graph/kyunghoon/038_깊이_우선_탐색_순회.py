from collections import defaultdict

adj_list = defaultdict(list)
visited = set()
result = []


def dfs(node):
    visited.add(node)
    result.append(node)
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(neighbor)


def solution(graph, start):
    for u, v in graph:
        adj_list[u].append(v)

    dfs(start)
    return result
