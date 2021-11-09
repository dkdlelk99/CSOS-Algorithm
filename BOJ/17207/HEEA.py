import sys

l=[]
result=[]
name=['Inseo', 'Junsuk', 'Jungwoo', 'Jinwoo', 'Youngki']
name.reverse()
for _ in range(10):
    swap=list(map(int, sys.stdin.readline().split()))
    l.append(swap)

for z in range(5):
    sum=0
    for i in range(5):
        start=0
        output=0
        for j in range(5,10):
            output+=(l[z][start]*l[j][i])
            start+=1
        sum+=output
    result.append(sum)

result.reverse()
print(name[result.index(min(result))])
