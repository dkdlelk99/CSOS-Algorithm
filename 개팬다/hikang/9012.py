import sys

T = int(sys.stdin.readline())

# '('랑 ')' 숫자 같으면 YES 출력되게
for i in range(T):
  list = sys.stdin.readline()
  for j in list:
    left="("
    right=")"
  if(list.count(left)==list.count(right)):
    print("YES")
  else:
    print("NO")
  