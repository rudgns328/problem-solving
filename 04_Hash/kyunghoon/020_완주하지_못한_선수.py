from collections import Counter


def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)

    for name, count in p.items():
        if c[name] != count:
            return name
