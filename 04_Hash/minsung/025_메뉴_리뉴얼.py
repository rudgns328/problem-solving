from itertools import combinations


def solution(orders, course):
    answer = []
    combo_count = {}

    for c in course:
        for order in orders:
            order = sorted(order)
            for combo in combinations(order, c):
                if combo not in combo_count:
                    combo_count[combo] = 1
                else:
                    combo_count[combo] += 1

    for c in course:
        counts = [combo_count[combo] for combo in combo_count if c == len(combo)]
        if counts:
            max_count = max(counts)

            if max_count >= 2:
                for combo in combo_count:
                    if len(combo) == c and combo_count[combo] == max_count:
                        answer.append("".join(combo))

    return sorted(answer)
