# 1920
import sys
input = sys.stdin.readline

int(input())
A = set(map(int, input().split()))
int(input())
B = list(map(int,input().split()))
for i in B:
    if i in A:
        print(1)
    else:
        print(0)
