def solution(numbers):
    s = 0
    for number in numbers:
        s += number
        
    answer = s / len(numbers)
    return answer