# 17219
# 성공

n, m = map(int, input().split())

p_dict = {}
for _ in range(n):
    site, pw= input().split()
    p_dict[site] = pw
    
for _ in range(m):
    print(p_dict[input()])
