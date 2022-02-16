M = int(input())
N = int(input())

eratos = [True] * (N + 1)
eratos[0], eratos[1] = False, False
prime = []
for i in range(N+1):
    if eratos[i]:
        if i >= M:
            prime.append(i)
        for j in range(i*2, N+1, i):
            eratos[j] = False

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime), min(prime), sep="\n")
