def solution(s):
    answer = 0
    check_dict = {")": "(", "]": "[", "}": "{"}
    o = "([{"
    open_list = [i for i in o]
    s_list = list(s)
    n = len(s_list)
    for _ in range(n):
        opened_list = []
        for i in range(n):

            if s_list[i] in open_list:
                opened_list.append(s_list[i])
            else:
                if not opened_list or opened_list.pop() != check_dict[s_list[i]]:
                    k = s_list.pop(0)
                    s_list.append(k)
                    break
                else:
                    if i == n - 1 and not opened_list:
                        answer += 1
                        k = s_list.pop(0)
                        s_list.append(k)
                    else:
                        continue

    return answer
