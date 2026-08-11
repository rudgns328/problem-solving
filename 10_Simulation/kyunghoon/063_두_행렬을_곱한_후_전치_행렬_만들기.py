def solution(matrix1, matrix2):
    res = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                res[i][j] += matrix1[j][k] * matrix2[k][i]
            
    return res

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))