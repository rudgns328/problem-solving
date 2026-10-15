def solution(brown, yellow):
    total = brown + yellow

    for h in range(1, int(total**0.5) + 1):
        if total % h == 0:
            w = total // h
            if w + h == (brown + 4) / 2:
                return [w, h]

    return []
