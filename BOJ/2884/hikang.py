H, M = map(int, input().split())

# 불필요한 0의 의미
# 00 <- 이 경우

if(M > 44):
  print(H, M - 45)
elif(M < 45 and H >= 1):
  print(H - 1 , M + 15)
else:
  print(23, M + 15)