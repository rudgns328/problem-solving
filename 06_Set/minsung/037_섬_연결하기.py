def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)
    return parents[x]


def union(x, y, parents, rank_data):
    x_root = find(x, parents)
    y_root = find(y, parents)

    if x_root != y_root:
        if rank_data[x_root] < rank_data[y_root]:
            parents[x_root] = y_root
        elif rank_data[x_root] > rank_data[y_root]:
            parents[y_root] = x_root
        else:
            parents[y_root] = x_root
            rank_data[x_root] += 1


def solution(n, costs):
    costs.sort(key=lambda x: x[2])

    parents = [i for i in range(n)]
    rank_data = [0] * n

    min_costs = 0
    edges = 0

    for edge in costs:
        if edges == n - 1:
            break

        x = find(edge[0], parents)
        y = find(edge[1], parents)

        if x != y:
            union(x, y, parents, rank_data)
            min_costs += edge[2]
            edges += 1

    return min_costs
