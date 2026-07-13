def solution(s):
    answer = []
    s = s[1:-1]
    groups = s.split("},{")
    groups[0] = groups[0][1:]
    groups[-1] = groups[-1][:-1]
    new_s = [[int(x) for x in g.split(",")] for g in groups]
    sorted_s = sorted(new_s, key=len)
    checked = set()
    answer.append(sorted_s[0][0])
    checked.add(sorted_s[0][0])
    for i in range(1, len(sorted_s)):
        for j in range(len(sorted_s[i])):
            if sorted_s[i][j] not in checked:
                answer.append(sorted_s[i][j])
                checked.add(sorted_s[i][j])
    return answer