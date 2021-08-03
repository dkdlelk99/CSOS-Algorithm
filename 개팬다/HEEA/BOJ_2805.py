n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)

start=1
end=l[len(l)-1]

while start<=end:
    print(start, end)
    c=0
    mid=(start+end)//2
    for i in l:
        result=i-mid
        if(result>0):
            c+=result
    if(c>=m):
        start=mid+1
    else:
        end=mid-1

print(end)