def solution(name):
    answer = 0
    n = len(name)

    for c in name:
        answer += min(ord(c) - ord("A"), 26 - (ord(c) - ord("A")))

    move = n - 1
    for i in range(n):
        next = i + 1
        while next < n and name[next] == "A":
            next += 1
        move = min(move, i * 2 + (n - next), i + (n - next) * 2)

    answer += move
    return answer
