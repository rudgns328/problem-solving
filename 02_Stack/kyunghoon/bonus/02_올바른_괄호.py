def solution(s):
    stack = []

    for c in s:
        if not stack and c == ")":
            return False
        if c == "(":
            stack.append(c)
        else:
            stack.pop()

    return len(stack) == 0
