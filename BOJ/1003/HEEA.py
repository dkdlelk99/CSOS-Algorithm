z=[-1]*41
z[0], z[1] = 1, 0
o=[-1]*41
o[0], o[1] = 0, 1

def fibo_zero(n): #0과 1의 경우에 대해서 조건을 나누어야 하지만 이미 초기화를 사전에 시켰으므로 안해도됨
    if(z[n]!=-1):
        return z[n]
    else:
        z[n]=fibo_zero(n-1)+fibo_zero(n-2)
        return z[n]

def fibo_one(n):
    if(o[n]!=-1):
        return o[n]
    else:
        o[n]=fibo_one(n-1)+fibo_one(n-2)
        return o[n]

t=int(input())
for i in range(t):
    n=int(input())
    print(fibo_zero(n), fibo_one(n))

