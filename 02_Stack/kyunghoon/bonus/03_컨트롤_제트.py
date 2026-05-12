def solution(s):
    stack = []
    for a in s.split():
        if a != "Z":
            stack.append(int(a))
        else:
            if stack:
                stack.pop()

    return sum(stack)
