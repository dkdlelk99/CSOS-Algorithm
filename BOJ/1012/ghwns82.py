# 1012

import sys
sys.setrecursionlimit(10**6)

def zombie(c):
    x,y = c[0], c[1]
    for i in [[x-1,y], [x,y-1], [x+1,y],[x,y+1]]:
        if i in cabbage:
            cabbage.remove(i)
            zombie(i)

for _ in range(int(input())):
    *a, n= map(int, input().split())
    cabbage = [list(map(int, input().split())) for _ in range(n)]
    worms = 0
    while cabbage:
        zombie(cabbage.pop())
        worms += 1
    print(worms)
