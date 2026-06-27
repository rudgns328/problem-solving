def solution(numbers, target):
    comb = []
    answer = 0
    def dfs(number, n):
        nonlocal answer
        comb.append(number)
        if n == len(numbers) - 1 and sum(comb) == target:
            answer += 1
            comb.pop()
            return
        elif n == len(numbers) - 1:
            comb.pop()
            return
        else:
            n += 1
            dfs(numbers[n], n)
            dfs(-numbers[n], n)
            comb.pop()
            
    dfs(numbers[0], 0)
    comb = []
    dfs(-numbers[0], 0)
    
    return answer

print(solution([4, 1, 2, 1], 4))