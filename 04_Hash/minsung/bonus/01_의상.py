from collections import Counter
from math import prod


def solution(clothes):
    counter = Counter(value for name, value in clothes)
    return prod(c + 1 for c in counter.values()) - 1
