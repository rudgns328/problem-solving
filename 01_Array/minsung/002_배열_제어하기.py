def solution(arr):
  unique_list = list(set(arr))
  unique_list.sort(reverse=True)
  return unique_list