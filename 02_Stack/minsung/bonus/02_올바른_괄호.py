def solution(s):
    answer = []
    for i in s:
        if i == "(":
            answer.append(i)
        elif i == ")":
            if not answer:
                return False
            else:
                answer.pop()
    if answer:
        return False
    else:
        return True
