for _ in range(int(input())):
    num = int(input())
    memo=[1,1,1]+[0]*97

    for i in range(3, num):
        memo[i]=memo[i-2] + memo[i-3]
    print(memo[num-1])
