def solution(arr, n):
    n %= 4
    arr_len = len(arr)
    
    for _ in range(n):
        new_arr = [[0] * arr_len for _ in range(arr_len)]
        for i in range(arr_len):
            for j in range(arr_len):
                new_arr[i][j] = arr[(arr_len - 1) - j][i]
        
        arr = new_arr
        
    return arr