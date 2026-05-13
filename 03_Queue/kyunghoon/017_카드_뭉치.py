def solution(cards1, cards2, goal):
    answer = ""
    one = []
    two = []
    for i in goal:
        if i in cards1:
            one.append(i)
        else:
            two.append(i)
    if cards1[: len(one)] == one and cards2[: len(two)] == two:
        answer = "Yes"
    else:
        answer = "No"
    return answer
