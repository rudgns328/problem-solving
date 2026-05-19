from collections import Counter


def solution(participant, completion):
    hash = Counter(participant)

    for c in completion:
        hash[c] -= 1

    for h in hash:
        if hash[h]:
            return h
