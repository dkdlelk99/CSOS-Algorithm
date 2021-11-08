memo = {0:(1,0), 1:(0,1)}
last_goal=2
for _ in range(int(input())):
    goal=int(input())
    for i in range(last_goal, goal+1):
        memo[i] = [x+y for x,y in zip(memo[i-1],memo[i-2])]
    print(memo[goal][0], memo[goal][1])
    last_goal=max(goal,2)
