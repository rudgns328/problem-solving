def solution(s):
    count = [0] * 26
    
    for c in s:
        count[ord(c) - ord("a")] += 1
        
    sorted_str = ""
    for i in range(26):
        sorted_str += chr(i + ord("a")) * count[i]

    return sorted_str