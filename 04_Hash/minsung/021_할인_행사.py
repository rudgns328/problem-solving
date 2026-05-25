def solution(want, number, discount):
    want_dic = dict(zip(want, number))
    answer = 0

    for i in range(len(discount) - 9):
        discount_dic = {}

        for j in range(i, i + 10):
            if discount[j] in want_dic:
                if discount[j] in discount_dic:
                    discount_dic[discount[j]] += 1
                else:
                    discount_dic[discount[j]] = 1

        if discount_dic == want_dic:
            answer += 1

    return answer
