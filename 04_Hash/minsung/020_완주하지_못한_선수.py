def solution(participant, completion):
    p = {}
    c = {}

    for i in participant:
        if i in p:
            p[i] += 1
        else:
            p[i] = 1

    for j in completion:
        if j in c:
            c[j] += 1
        else:
            c[j] = 1

    for k in p.keys():
        if k not in c or p[k] != c[k]:
            return k
