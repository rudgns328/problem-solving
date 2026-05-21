from collections import defaultdict, Counter


def solution(id_list, report, k):
    answer = []
    reporter_dict = defaultdict(set)

    for item in report:
        reporter, reported = item.split()
        reporter_dict[reporter].add(reported)

    reported_list = [
        reported for reports in reporter_dict.values() for reported in reports
    ]
    counter = Counter(reported_list)

    banned = {name for name, count in counter.items() if count >= k}

    for user in id_list:
        if user in reporter_dict:
            count = len([v for v in reporter_dict[user] if v in banned])
            answer.append(count)
        else:
            answer.append(0)

    return answer
