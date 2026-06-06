import sys

sys.setrecursionlimit(300000)


def preorder(node):
    if node is None:
        return []
    ret = [node["val"]]
    ret += preorder(node["left"])
    ret += preorder(node["right"])
    return ret


def postorder(node):
    if node is None:
        return []
    ret = postorder(node["left"])
    ret += postorder(node["right"])
    ret += [node["val"]]
    return ret


def insert(root, node):
    if node["x"] < root["x"]:
        if root["left"] is None:
            root["left"] = node
        else:
            insert(root["left"], node)
    else:
        if root["right"] is None:
            root["right"] = node
        else:
            insert(root["right"], node)


def solution(nodeinfo):
    answer = [[], []]

    nodes = list(enumerate(nodeinfo))
    nodes.sort(key=lambda x: (-x[1][1], x[1][0]))

    root = {"val": nodes[0][0] + 1, "x": nodes[0][1][0], "left": None, "right": None}

    for i in range(1, len(nodes)):
        node = {
            "val": nodes[i][0] + 1,
            "x": nodes[i][1][0],
            "left": None,
            "right": None,
        }
        insert(root, node)

    answer[0] = preorder(root)
    answer[1] = postorder(root)

    return answer
