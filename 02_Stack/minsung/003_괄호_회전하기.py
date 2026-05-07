def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        rotated = s[i:] + s[:i]
        
        stack = []
        is_valid = True
        
        for j in rotated:
            if j in "([{":
                stack.append(j)
            else:
                if not stack:
                    is_valid = False
                    break
                if j == ')' and stack[-1] == '(':
                    stack.pop()
                elif j == ']' and stack[-1] == '[':
                    stack.pop()
                elif j == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    is_valid = False
                    break
        
        if is_valid and not stack:
            answer += 1
        
    return answer