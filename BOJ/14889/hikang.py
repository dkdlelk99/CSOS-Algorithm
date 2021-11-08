import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
graph = []
team = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    team.append(i+1)

power = []

for i in combinations(team, n//2):
    # print(i)
    a = 0
    for j in combinations(i, 2):

        a += graph[j[0]-1][j[1]-1]+graph[j[1]-1][j[0]-1]
    power.append(a)

end = len(power)//2

start_team = power[:end]
end_team = power[end:]
end_team = end_team[::-1]

answer = 100 
for i in range(end):
    answer = min(answer, abs(start_team[i]-end_team[i]))

print(answer)
