def solution(enroll, referral, seller, amount):
    answer = []
    referral_dict = dict(zip(enroll, referral))
    enroll_dict = {}

    for i in range(len(enroll)):
        enroll_dict[enroll[i]] = 0

    for i in range(len(seller)):
        current = seller[i]
        money = amount[i] * 100

        while current != "-" and money >= 1:
            parent_money = money // 10
            enroll_dict[current] += money - parent_money
            current = referral_dict[current]
            money = parent_money

    for i in range(len(enroll)):
        answer.append(enroll_dict[enroll[i]])

    return answer
