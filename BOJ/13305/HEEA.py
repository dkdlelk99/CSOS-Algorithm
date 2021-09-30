n=int(input())
distance=list(map(int,input().split()))
money=list(map(int,input().split()))
money_min=money[0]
dp=[0]*(n-1)
dp[0]=money[0]*distance[0]
for i in range(1,n-1):
    if(money_min>money[i]):
        money_min=money[i]
        dp[i]=money[i]*distance[i]+dp[i-1]
    else:
        dp[i]=money_min*distance[i]+dp[i-1]

print(max(dp))
