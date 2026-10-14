def solution(s):
    answer = 0
    zeros = 0

    while s != "1":
        zeros += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        answer += 1

    return [answer, zeros]
