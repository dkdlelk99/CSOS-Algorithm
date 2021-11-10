import sys
from collections import Counter



# r, c, k 입력(첫쨋줄 입력)
r, c, k = map(int,sys.stdin.readline().split())
# 3X3 배열 입력(둘쨋줄 입력)
A = [list(map(int,sys.stdin.readline().split())) for _ in range(3)]



# R 연산
def R():
  copy_A = []
  max_len = 0
  for tmp in A:
    tmp = Counter(tmp)
    del (tmp[0])
    copy_A = sorted(tmp.items(),key=lambda x:(x[1],x[0]))
    tt = []
    for i in copy_A:
      tt.extend(i)
      if len(tt) == 100 :break
    max_len = max(max_len,len(tt))
    copy_A.append(tt)

  for ss in copy_A:
    ss += [0] * (max_len-len(ss))
  return copy_A

time = 0
while 1:
  if time > 100:
    break
  # A[r-1][c-1] == k 인 경우에
  
  if r<=len(A) and c<=len(A[0]) and A[r-1][c-1] == k:
    break
  if len(A)>=len(A[0]):
    A = R()
  else:
    A = list(map(list,zip(*A)))
    A = R()
    A = list(map(list,zip(*A)))
  
  time += 1
if time > 100:
  print(-1)
else:
  print(time)

