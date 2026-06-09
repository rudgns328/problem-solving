def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, cost, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            rank[root_a] += 1
        return cost
    return 0


def solution(n, costs):
    parent = list(range(n))
    rank = [0] * n
    total = 0

    costs.sort(key=lambda x: x[2])

    for a, b, cost in costs:
        total += union(a, b, cost, parent, rank)

    return total
