import sys
# input
N = int(sys.stdin.readline())
network = [[0]*N for i in range(N)]
connect = int(sys.stdin.readline())
# make graph with 2d list
for i in range(connect):
    a, b = map(int, sys.stdin.readline().split())
    network[a - 1][b - 1] = 1
    network[b - 1][a - 1] = 1

infected = [0]*N # infected computer = 1
infected[0] = 1


# find victims
def virus(index):
    for i in range(N):
        if network[index][i] == 1 and infected[i] == 0:
            infected[i] = 1
            virus(i)
    return


virus(0)
print(sum(infected) - 1)