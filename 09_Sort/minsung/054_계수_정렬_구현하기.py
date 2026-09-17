def solution(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    result = ""

    for i in range(26):
        char = chr(ord('a') + i)
        if char in count:
            result += char * count[char]

    return result