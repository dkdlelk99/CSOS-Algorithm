# 2609
a,b = map(int, input().split())
n1, n2, temp = max(a,b), min(a,b), 0
while 1:
    temp = n1% n2
    if not temp:
        break
    n1, n2 = n2, temp
print(n2)
print(a*b//n2)
