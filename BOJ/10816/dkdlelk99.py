import sys
# Input
N = int(sys.stdin.readline())
pocket = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
# make dictionary structure
dictPocket = dict()
for i in pocket:
    if i in dictPocket.keys():
        dictPocket[i] += 1
    else:
        dictPocket[i] = 1
# make answer
answer = ""
for i in check:
    if i in dictPocket.keys():
        answer += str(dictPocket[i]) + " "
    else:
        answer += "0 "
# output
print(answer[:-1])
