N = int(input())
arr = [i for i in range(1, N+1)]

# 현재 pointer와 엔드 포인터
ptr, end = 0,0
cnt = 0

for i in range(N):

  while end<N and ptr<N:
    ptr += arr[end]
    end +=1
  if ptr == N:
    cnt +=1
  ptr -= arr[i]

print(cnt)
