from collections import defaultdict, deque

adj_list = defaultdict(list)
visited = set()
answer = []


def bfs(start):
    queue = deque([start])
    visited.add(start)
    answer.append(start)

    while queue:
        node = queue.popleft()

        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                answer.append(neighbor)


def solution(graph, start):
    for u, v in graph:
        adj_list[u].append(v)
    bfs(start)
    return answer
