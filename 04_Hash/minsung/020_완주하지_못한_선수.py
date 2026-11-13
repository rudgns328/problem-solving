from collections import Counter


def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    return list(diff.keys())[0]
