# 1010
def fac(n):
    if n<=1:
        return 1
    return fac(n-1)*n

for _ in range(int(input())):
    r, n = map(int, input().split())
    print(fac(n)// fac(r)//fac(n-r))
