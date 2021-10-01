import sys
n,k=map(int,sys.stdin.readline().split())
p=1000000007
l=[1]*(n+1) #인덱스 1번부터 사용하기 위해, 하나 더 크게 할당한다.
for i in range(2,n+1): #계속해서 곱하다 보면 int가 가질 수 있는 범위를 넘어서게 되면서 오버플로우가 발생함, 따라서 곱하면서 p를 나누어주어야 함
    l[i]=l[i-1]*i%p

def check(n,k): #계속해서 곱하다 보면 int가 가질 수 있는 범위를 넘어서게 되면서 오버플로우가 발생함, 따라서 곱하면서 p를 나누어주어야 함
    if(k==0):
        return 1
    elif(k%2==0):
        y=check(n,k//2)
        return y*y%p
    else:
        y=check(n,(k-1)//2)
        return y*y*n%p

print(l[n]*(check(l[k]*l[n-k],p-2)%p)%p)
