def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            max_land = 0
            for k in range(4):
                if k != j:
                    max_land = max(max_land, land[i - 1][k])
            land[i][j] += max_land

    return max(land[-1])
