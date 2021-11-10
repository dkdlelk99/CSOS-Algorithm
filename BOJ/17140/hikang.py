import sys
import time
from collections import Counter



# r, c, k 입력(첫쨋줄)
r, c, k = map(int,sys.stdin.readline().split())
# 3X3 배열 입력(둘쨋줄)
for _ in range(3):
  A = list(map(int,sys.stdin.readline().split()))

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
# C 연산은 언제하는지 모르겠음..
# def C():


# 코드 실행 시작점
start = time.time()

# A[r][c] 연산을 시작
def main():
  if A[r][c] == k and (time.time()-start <= 10000):
    print("소요된 시간은 : ",time.time()-start)
  else:
    print("-1")
