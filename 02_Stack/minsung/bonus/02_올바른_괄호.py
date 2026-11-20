def solution(s):
    answer = []
    for c in s:
        if c == "(":
            answer.append(c)
        elif answer:
            answer.pop()
        else:
            return False
    return not answer
