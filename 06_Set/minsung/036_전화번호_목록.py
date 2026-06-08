def solution(phone_book):
    set_phone = set(phone_book)

    for phone in phone_book:
        for length in range(1, len(phone)):
            if phone[:length] in set_phone:
                return False

    return True
