def solution(clothes):
    answer = 1
    closet = {}

    for c in clothes:
        if c[1] in closet:
            closet[c[1]] += 1
        else:
            closet[c[1]] = 1

    for v in closet.values():
        answer *= v + 1

    return answer - 1
