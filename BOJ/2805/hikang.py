import sys

# N 나무의 갯수, M 절단기 설정 높이
N, M = map(int,sys.stdin.readline().split())
height_list = list(map(int,sys.stdin.readline().split()))

start, max_height = 1, max(height_list)

# while문 : 높이 구함
while start <= max_height:
  mid = (start+max_height)//2

  tmp = 0
  for i in height_list:
    if i >= mid:
      tmp += i - mid
    # 이분탐색 알고리즘
    if tmp>=M:
      start = mid + 1
    else:
      max_height = mid - 1

print(max_height)
