import sys
# input
N = int(sys.stdin.readline())
p = sorted(list(map(int, sys.stdin.readline().split())))
# make answer
answer, each_time = 0, 0
for i in p:
    each_time += i
    answer += each_time
print(answer)