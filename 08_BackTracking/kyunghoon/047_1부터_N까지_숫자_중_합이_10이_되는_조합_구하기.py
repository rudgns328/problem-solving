def solution(N):
    result = []
    combination = []

    def backtrack(start, current_sum):
        for num in range(start, N + 1):
            new_sum = current_sum + num
            
            if new_sum == 10:
                combination.append(num)
                result.append(combination[:])
                combination.pop()
                break
            elif new_sum > 10:
                break
            
            combination.append(num)
            backtrack(num + 1, new_sum)
            combination.pop()
            
    backtrack(1, 0)            
    return result