from collections import defaultdict


def solution(info, edges):
    tree = defaultdict(list)

    for parent, child in edges:
        tree[parent].append(child)

    def dfs(node, sheep, wolf, next_nodes):
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1

        if sheep <= wolf:
            return 0

        next_nodes = next_nodes + tree[node]
        max_sheep = sheep

        for next_node in next_nodes:
            result = dfs(
                next_node, sheep, wolf, [n for n in next_nodes if n != next_node]
            )
            max_sheep = max(max_sheep, result)

        return max_sheep

    return dfs(0, 0, 0, [])
