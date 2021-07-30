import sys
# input
N = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
# make Seive of Eratosthenes [2, max] (max = max input value)
len_e = max(check) + 1
eratos = [True] * len_e
eratos[0], eratos[1] = False, False
prime = []
for i in range(len_e):
    if eratos[i]:
        prime.append(i)
        for j in range(i*2, len_e, i):
            eratos[j] = False
# solve with Seive
answer = 0
for i in check:
    if i in prime:
        answer += 1
# output
print(answer)