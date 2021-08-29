a, b = map(int,input().split())

data = []

# a와 b를 나누었을때 나머지가 0이 되는 리스트를 만들고
# 그 리스트중에서 가장 큰 값을 뽑기
for i in range(1, a+1):
  if(a%i == 0) & (b%i == 0):
    data.append(i)

# 최대 공약수 = 리스트 최댓값
print(max(data))
# 최소 공배수 = 두수를 곱하고 최대공약수 나누기
print(a*b//max(data))