import sys

n,new,p=map(int, sys.stdin.readline().split())
score=list(map(int,sys.stdin.readline().split()))
score.append(new)
score.sort(reverse=True)
sum=0
copy_score=score.copy()
if(score[len(score)-1]==new):
    print(-1)
else:
    for i in score:
        copy_score=[j for j in copy_score if j!=i]
        sum+=1
        if(i==new):
            break
    print(sum)