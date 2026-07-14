def solution(s):
    s = s[2:-2].split("},{")
    new_s = [[int(x) for x in g.split(",")] for g in s]
    sorted_s = sorted(new_s, key=len)
    
    answer = []
    checked = set()
    
    for group in sorted_s:
        for num in group:
            if num not in checked:
                answer.append(num)
                checked.add(num)

    return answer