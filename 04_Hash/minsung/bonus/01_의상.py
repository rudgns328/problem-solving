def solution(clothes):
    answer = 1
    clothes_dict = {}

    for c in clothes:
        if c[1] not in clothes_dict:
            clothes_dict[c[1]] = 1
        else:
            clothes_dict[c[1]] += 1

    values = list(map(lambda x: x + 1, clothes_dict.values()))

    for v in values:
        answer *= v

    return answer - 1
