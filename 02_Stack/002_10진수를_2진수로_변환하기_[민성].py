decimal1 = 10
decimal2 = 27
decimal3 = 12345

def solution(decimal):
  stack = []
  while decimal > 0:
    remainder = decimal % 2
    stack.append(str(remainder))
    decimal = decimal // 2
  binary = ""

  while stack:
    binary += stack.pop()
    
  return binary

print(solution(decimal3))