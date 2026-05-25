def solution(msg):
    answer = []
    chr_dic = {}

    for i in range(26):
        chr_dic[chr(65 + i)] = i + 1

    w = ""
    for i in range(len(msg)):
        if w + msg[i] not in chr_dic:
            answer.append(chr_dic[w])
            chr_dic[w + msg[i]] = len(chr_dic) + 1
            w = msg[i]
        else:
            w = w + msg[i]

    answer.append(chr_dic[w])

    return answer
