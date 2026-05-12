def solution(s):
    stack = []
    for i in s:
        if not stack and i == ")":
            return False
        elif i == "(":
            stack.append(i)
        elif i == ")":
            stack.pop()

    if stack:
        return False
    else:
        return True
