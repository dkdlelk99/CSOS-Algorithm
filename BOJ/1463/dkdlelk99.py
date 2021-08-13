import sys

answer = [0] * 1000001

for i in range(2, 1000001):
    answer[i] = answer[i-1] + 1 # rule 1 ( -1 )
    if i%2 == 0:
        answer[i] = min(answer[i], answer[int(i/2)]+1) # rule 2 ( /2 )
    if i%3 == 0:
        answer[i] = min(answer[i], answer[int(i/3)]+1) # rule 3 ( /3 )
# input
X = int(sys.stdin.readline())
print(answer[X])