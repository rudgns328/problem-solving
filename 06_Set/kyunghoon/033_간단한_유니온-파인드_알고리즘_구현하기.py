def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union_set(x, y, parents, rank_data):
    root1 = find(parents, x)
    root2 = find(parents, y)

    if root1 != root2:
        if rank_data[root1] < rank_data[root2]:
            parents[root1] = root2
        elif rank_data[root1] > rank_data[root2]:
            parents[root2] = root1
        else:
            parents[root2] = root1
            rank_data[root1] += 1


def solution(k, operations):
    parents = list(range(k))
    rank_data = [0] * k

    results = []
    for op in operations:
        if op[0] == "u":
            x = int(op[1])
            y = int(op[2])
            union_set(x, y, parents, rank_data)
        elif op[0] == "f":
            x = int(op[1])
            y = int(op[2])
            results.append(find(parents, x) == find(parents, y))

    return results
