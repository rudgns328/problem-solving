def solution(brown, yellow):
    sum = brown + yellow
    num = 1
    new_sum = 0
    while True:
        if sum % num != 0:
            num += 1
            continue
        new_sum = sum // num
        if new_sum < brown and new_sum + (num * 2 - 2) + (new_sum - 2) == brown:
            break
        num += 1
        
    return [new_sum, num]