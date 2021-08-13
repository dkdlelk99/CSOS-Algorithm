import sys
# input
X = int(sys.stdin.readline())
cnt = 0
while(X != 1 and X>0):
    if X%3 == 0:
        X = X//3
        cnt += 1
    elif X%3 == 1:
        X -= 1
        cnt += 1
    elif X%2 == 0:
        X = X//2
        cnt += 1
    else:
        X -= 1
        cnt += 1
print(cnt)
