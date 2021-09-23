import sys

n=int(sys.stdin.readline())

if(n**0.5==int(n**0.5)):
    print(int(n**0.5))
else:
    print(int(n**0.5)+1)
