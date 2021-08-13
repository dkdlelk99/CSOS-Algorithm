n=int(input())
l=[]
answer=[]

for i in range(n):
    x=int(input())
    if(x==0):
        if(len(l)!=0):
            answer.append(max(l))
            l.remove(max(l))
