def solution(id_list, report, k):
    answer = []
    report = list(set(report))

    reported_count = {}
    for r in report:
        reporter, reported = r.split()
        if reported not in reported_count:
            reported_count[reported] = 1
        else:
            reported_count[reported] += 1

    user_reported_list = {}

    for id in id_list:
        user_reported_list[id] = []
    for r in report:
        reporter, reported = r.split()
        user_reported_list[reporter].append(reported)

    banned_user = set()
    for reported, count in reported_count.items():
        if count >= k:
            banned_user.add(reported)

    for id in id_list:
        mail_count = 0
        for reported in user_reported_list[id]:
            if reported in banned_user:
                mail_count += 1
        answer.append(mail_count)

    return answer
