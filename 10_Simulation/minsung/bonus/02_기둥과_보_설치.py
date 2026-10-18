def solution(n, build_frame):
    structures = set()

    for x, y, a, b in build_frame:
        if b == 1:
            if is_valid(structures, x, y, a):
                structures.add((x, y, a))
        else:
            structures.remove((x, y, a))

            for sx, sy, sa in structures:
                if not is_valid(structures, sx, sy, sa):
                    structures.add((x, y, a))
                    break

    return sorted(structures, key=lambda x: (x[0], x[1], x[2]))


def is_valid(structures, x, y, a):
    if a == 0:
        return (
            y == 0
            or (x, y - 1, 0) in structures
            or ((x - 1, y, 1) in structures or (x, y, 1) in structures)
        )
    else:
        return ((x, y - 1, 0) in structures or (x + 1, y - 1, 0) in structures) or (
            (x - 1, y, 1) in structures and (x + 1, y, 1) in structures
        )
