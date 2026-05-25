def solution(record):
    answer = []
    uid_dic = {}

    for r in record:
        data = r.split()
        if data[0] == "Enter":
            uid_dic[data[1]] = data[2]
        elif data[0] == "Change":
            uid_dic[data[1]] = data[2]

    for r in record:
        data = r.split()
        if data[0] == "Enter":
            answer.append(f"{uid_dic[data[1]]}님이 들어왔습니다.")
        elif data[0] == "Leave":
            answer.append(f"{uid_dic[data[1]]}님이 나갔습니다.")

    return answer
