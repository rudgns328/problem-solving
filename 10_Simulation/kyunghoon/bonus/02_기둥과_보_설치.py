def solution(n, build_frame):
    pillar = set()
    beam = set()
    
    def check_pillar(x, y):
        if y == 0:
            return True
        if (x, y - 1) in pillar:
            return True
        if (x, y) in beam or (x - 1, y) in beam:
            return True
        return False
    
    def check_beam(x, y):
        if (x, y - 1) in pillar or (x + 1, y - 1) in pillar:
            return True
        if (x - 1, y) in beam and (x + 1, y) in beam:
            return True
        return False
    
    def check_all():
        for px, py in pillar:
            if not check_pillar(px, py):
                return False
        for bx, by in beam:
            if not check_beam(bx, by):
                return False
        return True

    for x, y, a, b in build_frame:
        if b == 1:
            if a == 0:
                if check_pillar(x, y):
                    pillar.add((x, y))
            else:
                if check_beam(x, y):
                    beam.add((x, y))
        else:
            if a == 0:
                if (x, y) in pillar:
                    pillar.remove((x, y))
                    if not check_all():
                        pillar.add((x, y))
            else:
                if (x, y) in beam:
                    beam.remove((x, y))
                    if not check_all():
                        beam.add((x, y))

    answer = [[x, y, 0] for x, y in pillar] + [[x, y, 1] for x, y in beam]
    result = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return result