k,n=map(int,input().split())
l=[]
for i in range(k):
    l.append(int(input()))
l=sorted(l)
c=0

start=1
end=l[len(l)-1]

while start<=end:
    mid=(start+end)//2
    c=0
    for i in l:
        c+=i//mid
    if(c>=n):
        start=mid+1
    else:
        end=mid-1

print(end)