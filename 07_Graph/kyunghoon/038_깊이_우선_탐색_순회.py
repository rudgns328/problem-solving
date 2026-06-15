from collections import defaultdict


def dfs(node, visited, current_node, answer):
    visited[current_node] = True
    answer.append(current_node)
    for adj_node in node[current_node]:
        if not visited[adj_node]:
            dfs(node, visited, adj_node, answer)


def solution(graph, start):
    all_nodes = set()
    for i in graph:
        for j in i:
            all_nodes.add(j)
    visited = {k: False for k in all_nodes}

    node = defaultdict(list)
    for k, v in graph:
        node[k] += [v]

    answer = []

    dfs(node, visited, start, answer)

    return answer
