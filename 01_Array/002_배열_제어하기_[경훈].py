def solution(lst):
    unique_lst = list(set(lst))
    unique_lst.sort(reverse=True)
    return unique_lst