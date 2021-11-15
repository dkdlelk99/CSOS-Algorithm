import sys


#   N  |  0  |  1  |  2  |  3  |  4  |  5  |
# zero |  1  |  0  |  1  |  1  |  2  |  3  |
#  one |  0  |  1  |  1  |  2  |  3  |  5  |

# 규칙 : zero = 1, 0, 1 // one = 0, 1, 1
# 그 이후 N2 = N1 + N0

T = int(sys.stdin.readline())
for i in range(T):
  N = int(sys.stdin.readline())
  zero = [1,0,1]
  one = [0,1,1]
  #N2 부터 규칙을 적용할 수 있음
  if N >= 3:
    for i in range(3, N+1):
      zero.append(zero[i-1]+zero[i-2])
      one.append(one[i-1]+one[i-2])
  print(zero[N],one[N])
