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


def solution(k, operations):
    parents = list(range(k))
    rank_data = [0] * k
    answer = []

    for o in operations:
        if o[0] == "u":
            x = int(o[1])
            y = int(o[2])
            union(x, y, parents, rank_data)
        elif o[0] == "f":
            x = int(o[1])
            y = int(o[2])
            answer.append(find(x, parents) == find(y, parents))

    return answer
