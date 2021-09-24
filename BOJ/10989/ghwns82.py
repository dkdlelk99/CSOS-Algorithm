import sys
input = sys.stdin.readline
N= int(input())
num=[0]*10_000

for _ in range(N):
    num[int(input())-1] +=1

for i,v in enumerate(num):
    if v:
        for _ in range(v):
            print(i+1)
