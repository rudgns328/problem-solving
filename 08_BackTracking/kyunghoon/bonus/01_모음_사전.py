def solution(word):
    vowels = "AEIOU"
    answer = 0
    found = False
    
    def dfs(current):
        nonlocal answer, found
        if current == word:
            found = True
            return
        if len(current) == 5:
            return
        for v in vowels:
            answer += 1
            dfs(current + v)
            if found:
                return
            
    dfs("")
    
    return answer