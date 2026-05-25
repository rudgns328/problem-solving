def solution(msg):
    answer = []
    alpha = {chr(i): i - 64 for i in range(65, 91)}
    n = 26
    i = 1
    while msg:
        if len(msg) == 1 or i > len(msg):
            answer.append(alpha[msg])
            msg = ""
            break
        elif msg[:i] in alpha:
            i += 1
            continue
        else:
            answer.append(alpha[msg[: i - 1]])
            alpha[msg[:i]] = n + 1
            n += 1
            msg = msg[i - 1 :]
            i = 1

    return answer
