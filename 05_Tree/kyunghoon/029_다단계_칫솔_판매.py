def solution(enroll, referral, seller, amount):
    answer = []

    dict = {c: {"parent": p, "price": 0} for c, p in zip(enroll, referral)}

    for i in range(len(seller)):
        dict[seller[i]]["price"] += amount[i] * 100
        current = seller[i]
        earn = int(amount[i] * 100 * 0.1)

        while dict[current]["parent"] != "-":
            p = dict[current]["parent"]

            if earn < 1:
                break

            dict[current]["price"] -= earn
            dict[p]["price"] += earn
            current = p
            earn = int(earn * 0.1)

        if earn >= 1:
            dict[current]["price"] -= earn

    for c in dict:
        answer.append(dict[c]["price"])

    return answer
