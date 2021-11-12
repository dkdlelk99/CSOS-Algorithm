import sys

n=int(sys.stdin.readline())
search=sys.stdin.readline().strip()
search=search.replace(" ","")

arr=[0]*n
isused=[False]*(n+1)
l=[]

def func(k):
    if(k==n):
        st=""
        for i in range(n):
            st+=str(arr[i])
        l.append(st)
    for i in range(1, n+1):
        if(isused[i]==False):
            arr[k]=i
            isused[i]=True
            func(k+1)
            isused[i]=False

func(0)

if(l.index(search)==(len(l)-1)):
    print(-1)
else:
    for i in l[l.index(search)+1]:
        print(i, end= " ")