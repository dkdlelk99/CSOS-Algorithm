import sys

N = int(sys.stdin.readline())
arr_N = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr_M = list(map(int,sys.stdin.readline().split()))

dict=dict()

for i in arr_N:
  # arr_N == [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
  # dict == {6:"1", 3:"2", 2:"1", 10:"3", -10:"2", 7:"1"}
  try:
    dict[i] += 1
  except:
    dict[i] = 1

for i in arr_M:
  # 가지고 있는 숫자 카드 dict[i]의 값을 print
  try:
    print(dict[i], end=" ")
  except:
    print(0, end=" ")