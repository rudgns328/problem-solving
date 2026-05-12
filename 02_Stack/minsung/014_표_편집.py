def solution(n, k, cmd):
    delete = []
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]
    k = k + 1

    for cmd_i in cmd:
        if cmd_i == "C":
            delete.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]

        elif cmd_i == "Z":
            restore = delete.pop()
            up[down[restore]] = restore
            down[up[restore]] = restore

        else:
            action, num = cmd_i.split()
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]

    answer = ["O"] * n
    for i in delete:
        answer[i - 1] = "X"

    return "".join(answer)
