A = int(input())
B = int(input())
C = int(input())

mul = str(A*B*C)

# 0~9 count해서 출력
for i in range(10):
  print(mul.count(str(i)))