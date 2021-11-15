b = [list(map(int, input().split())) for _ in range(int(input()))]  
for i,v in enumerate(b[1:],1):
    v[0] += min(b[i-1][1], b[i-1][2])
    v[1] += min(b[i-1][0], b[i-1][2])
    v[2] += min(b[i-1][1], b[i-1][0])
print(min(v))
