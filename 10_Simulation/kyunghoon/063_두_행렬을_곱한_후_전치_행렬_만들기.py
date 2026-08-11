def solution(matrix1, matrix2):
    res = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            total = 0
            for k in range(3):
                total += matrix1[j][k] * matrix2[k][i]
            res[i][j] = total
            
    return res