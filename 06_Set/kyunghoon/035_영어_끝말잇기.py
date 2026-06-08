def solution(n, words):
    answer = []
    check = []
    for i in range(len(words)):

        if i != 0:
            a = words[i]
            b = words[i - 1]

            if a[0] != b[-1] or a in check:
                answer += [len(check) % n + 1, len(check) // n + 1]
                break
        check.append(words[i])
    if answer:
        return answer
    else:
        return [0, 0]
