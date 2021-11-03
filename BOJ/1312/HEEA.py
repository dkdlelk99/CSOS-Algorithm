import sys

a,b,n=map(int,sys.stdin.readline().split())
result=a%b

for _ in range(n-1):
    result=(result*10)%b

print((result*10)//b)