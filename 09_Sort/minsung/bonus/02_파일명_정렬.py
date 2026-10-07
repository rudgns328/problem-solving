def solution(files):
    answer = []

    for i, file in enumerate(files):
        for j, char in enumerate(file):
            if char.isdigit():
                head = file[:j]
                number = ""
                for k in range(j, min(j + 5, len(file))):
                    if file[k].isdigit():
                        number += file[k]
                    else:
                        break
                break

        answer.append((head.lower(), int(number), i, file))

    answer.sort(key=lambda x: (x[0], x[1]))
    return [x[3] for x in answer]
