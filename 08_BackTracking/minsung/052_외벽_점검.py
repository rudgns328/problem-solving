from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)

    for i in range(length):
        weak.append(weak[i] + n)

    dist.sort(reverse=True)

    for perm in permutations(dist):
        for start in range(length):
            count = 1
            cover = weak[start] + perm[0]

            for i in range(start, start + length):
                if weak[i] > cover:
                    count += 1
                    if count > len(perm):
                        break
                    cover = weak[i] + perm[count - 1]
            else:
                answer = min(answer, count)

    return answer if answer <= len(dist) else -1
