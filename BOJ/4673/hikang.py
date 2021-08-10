# 생성자 구현
def d(n):
  return n + sum(map(int,str(n)))

sNum = set()
# 생성자가 있는 경우에 sNum 집합에 추가
for i in range(1,10001):
  a = d(i)
  if a < 10001:
    sNum.add(a)

# sNum 집합에 없으면 셀프넘버라는 의미
# 범위 전체에서 셀프넘버인 경우 출력
for i in range(1,10001):
  if i not in sNum:
    print(i)
