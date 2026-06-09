from collections import defaultdict

adj_list = defaultdict(list)
visited = set()
answer = []


def dfs(node):
    visited.add(node)
    answer.append(node)

    for neighbor in adj_list.get(node, []):
        if neighbor not in visited:
            dfs(neighbor)


def solution(graph, start):
    for u, v in graph:
        adj_list[u].append(v)
    dfs(start)
    return answer
