from collections import defaultdict, deque


def solution(info, edges):
    pc = defaultdict(list)
    max_sheep = 1
    for p, c in edges:
        pc[p].append(c)

    queue = deque([(0, 1, 0, pc[0])])
    while queue:
        node, sheep, wolf, next_nodes = queue.popleft()
        if wolf >= sheep:
            continue

        next_nodes = next_nodes + pc[node]
        for next_node in next_nodes:
            new_next = [n for n in next_nodes if n != next_node]
            new_sheep = sheep + (1 if info[next_node] == 0 else 0)
            new_wolf = wolf + (1 if info[next_node] == 1 else 0)
            max_sheep = max(max_sheep, new_sheep)
            queue.append((next_node, new_sheep, new_wolf, new_next))

    return max_sheep
