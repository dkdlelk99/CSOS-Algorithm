result=[]
result.append(0)
result.append(1)
for i in range(1,45):
    result.append(result[i]+result[i-1])
n=int(input())
print(result[n])
