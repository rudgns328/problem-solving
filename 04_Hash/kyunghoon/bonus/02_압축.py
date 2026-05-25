def solution(msg):
    answer = []
    alpha = {chr(i): i - 64 for i in range(65, 91)}
    n = 27
    w = ""

    for c in msg:
        if w + c in alpha:
            w += c
        else:
            answer.append(alpha[w])
            alpha[w + c] = n
            n += 1
            w = c

    answer.append(alpha[w])

    return answer
