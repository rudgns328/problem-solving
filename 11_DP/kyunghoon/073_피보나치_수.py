def solution(n):
    fibodata = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i < 3:
            fibodata[i] = 1
        else:
            fibodata[i] = fibodata[i-1] + fibodata[i-2]
    
    return fibodata[n] % 1234567