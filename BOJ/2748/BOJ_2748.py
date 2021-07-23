result=[]
result.append(0)
result.append(1)
for i in range(1,1000000000000000000):
    result.append((int(result[i]+result[i-1])%1000000))
n=int(input())
print(result[n])

