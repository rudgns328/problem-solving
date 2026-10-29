def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    answer = n - len(lost_set)

    for student in sorted(lost_set):
        for neighbor in (student - 1, student + 1):
            if neighbor in reserve_set:
                reserve_set.remove(neighbor)
                answer += 1
                break

    return answer
