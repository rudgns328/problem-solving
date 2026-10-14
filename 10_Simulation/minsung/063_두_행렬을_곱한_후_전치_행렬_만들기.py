def multiply_matrices(matrix1, matrix2):
    n = len(matrix1)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def transpose_matrix(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][i] = matrix[i][j]

    return result


def solution(matrix1, matrix2):
    mutiplied = multiply_matrices(matrix1, matrix2)
    transposed = transpose_matrix(mutiplied)
    return transposed
