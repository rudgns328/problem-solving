def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s = sorted(s, key=lambda x: len(x))

    for n in s:
        numbers = n.split(",")
        for number in numbers:
            if int(number) not in answer:
                answer.append(int(number))
    return answer
