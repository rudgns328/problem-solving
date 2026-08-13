def solution(s):
    answer = []
    times = 0
    counts = 0
    
    while s != '1':
        counts += s.count('0')
        length = len(s.replace('0', ''))
        s = format(int(length), 'b')
        times += 1
        
    answer.extend([times, counts])    
    return answer

print(solution("01110"))