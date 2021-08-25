N = list(map(int,input()))

arr = [0] * 10

for i in range(len(N)):
  n = int(N[i])

  # 예외사항 : 방 숫자가 6 또는 9인 경우
  if n == 6 or n == 9:
    # 인덱스 더 작은 값 가지는 곳에 + 1
    if arr[6] <= arr[9]:
      arr[6] += 1
    else:
      arr[9] += 1

  # 이외의 경우는 해당하는 구간에 +1
  else:
    arr[n] += 1

# 인덱스 최대 값 = 필요한 세트의 최소 개수
print(max(arr))