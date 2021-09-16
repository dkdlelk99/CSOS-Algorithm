import sys
import itertools

height=[]
for _ in range(9):
    height.append(int(sys.stdin.readline()))

height.sort()

combi=list(itertools.combinations(height,7))
result=[]
for i in combi:
    sum=0
    for j in i:
        sum+=j
    if(sum==100):
        result.append(i)

for i in result[0]:
    print(i)