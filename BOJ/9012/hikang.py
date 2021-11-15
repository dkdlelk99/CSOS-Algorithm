import sys

T = int(sys.stdin.readline())

# stack 사용해서 '(' 들어오면 append
# ')' 들어오면 pop
for i in range(T):
  list = sys.stdin.readline()
  stack = []

  for j in list:
    if j == "(":
      stack.append(j)
    elif j == ")":
      # 조건을 생각하지 못해서
      # https://greedysiru.tistory.com/270
      # 위 사이트 참고
      if len(stack) != 0 and stack[-1] == "(":
        stack.pop()
      else:
        stack.append(")")
        break
  
  if len(stack) == 0:
    print("YES")
  else:
    print("NO")