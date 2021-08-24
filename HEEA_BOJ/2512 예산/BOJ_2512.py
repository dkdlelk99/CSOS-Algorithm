n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
m=int(input())

start=1
end=l[len(l)-1]

while start<=end:
    mid=(start+end)//2
    c=0
    for i in l:
        if(i>mid):
            c+=mid
        else:
            c+=i
    if(c<=m):
        start=mid+1
    else:
        end=mid-1
print(end)