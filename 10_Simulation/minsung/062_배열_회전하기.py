def rotate(arr):
    n = len(arr)
    new_arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_arr[j][n - 1 - i] = arr[i][j]

    return new_arr


def solution(arr, n):
    rotated_arr = arr.copy()
    for _ in range(n):
        rotated_arr = rotate(rotated_arr)

    return rotated_arr
