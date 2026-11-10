def solution(k, tangerine):
    answer = 0
    count = {}

    for t in tangerine:
        if t in count:
            count[t] += 1
        else:
            count[t] = 1

    sorted_count = sorted(count.values(), reverse=True)

    for i in sorted_count:
        k -= i
        answer += 1
        if k <= 0:
            break

    return answer
