import sys

N = int(sys.stdin.readline())
point = 666

# 브루트포스 알고리즘
while True:
    if '666' in str(point):
        N -= 1     
    if N == 0: 
        break
    point += 1

print(point)  