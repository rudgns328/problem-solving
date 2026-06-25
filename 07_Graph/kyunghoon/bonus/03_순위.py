def solution(n, results):
    answer = 0
    record = [[0] * (n + 1) for _ in range(n + 1)]
        
    for a, b in results:
        record[a][b] = 1
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if record[i][k] == 1:
                    if record[k][j] == 1:
                        record[i][j] = 1
    
    for i in range(1, n + 1):
        count = sum(record[i][j] + record[j][i] for j in range(1, n + 1))
        if count == n - 1:
            answer += 1
            
    return answer