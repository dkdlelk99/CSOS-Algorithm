N, r, c = map(int,input().split())

width = 2**N
max_val = 2**(2*N)

calc = []

for i in range(N):
    half = width // 2

    if r >= half and c >= half:
        r -= half
        c -= half
        calc.append(3)
    elif r >= half and c < half:
        r -= half
        calc.append(2)
    elif r < half and c >= half:
        c -= half
        calc.append(1)
    else:
        calc.append(0)

    width //= 2

answer = 0
for i in range(N):
    answer += 4**(N-i-1) * calc[i]
print(answer)