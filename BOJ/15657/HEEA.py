n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)

arr=[0]*n

def func(k,index):
    if(k==m):
        for i in range(m):
            print(arr[i],end=" ")
        print("")
        return
    for i in range(index,len(l)):
        arr[k]=l[i]
        func(k+1,i)

func(0,0)
