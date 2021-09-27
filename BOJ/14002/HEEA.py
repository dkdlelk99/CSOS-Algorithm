n=int(input())
a=list(map(int,input().split()))
dp=[1]*n
dp1=[0]*n
output=[]

for i in range(1,n):
    count=0
    for j in range(i):
        if(a[i]>a[j] and count<dp[j]):
            count=dp[j]
            swap=list(filter(lambda x: a[x]==a[j], range(i)))
            if(len(swap)>=2):
               dp1[i]=swap[len(swap)-1]
            else:
                dp1[i]=j
            dp[i]+=1

start=dp.index(max(dp))

for i in range(max(dp)):
    output.append(a[start])
    start=dp1[start]
output=sorted(output)

print(max(dp))
for i in output:
    print(i,end=" ")
