def solution(record):
    names = {}
    result = []

    for r in record:
        e = r.split()
        if len(e) < 3:
            continue
        uid, name = e[1], e[2]
        names[uid] = name

    for cmd in record:
        c = cmd.split()
        if c[0] == "Enter":
            result.append(names[c[1]] + "님이 들어왔습니다.")
        elif c[0] == "Leave":
            result.append(names[c[1]] + "님이 나갔습니다.")

    return result
