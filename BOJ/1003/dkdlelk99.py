import sys
# initialize [0,0] answer list
answer = [[0,0] for i in range(41)]
answer[0][0], answer[1][1] = 1, 1
# make answer
for i in range(2,41):
    answer[i][0] = answer[i-1][0] + answer[i-2][0]
    answer[i][1] = answer[i - 1][1] + answer[i - 2][1]
# input
T = int(sys.stdin.readline())
# solve
for _ in range(T):
    N =int(sys.stdin.readline())
    print(answer[N][0], answer[N][1])
