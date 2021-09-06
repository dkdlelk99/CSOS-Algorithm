# 11653
def factorization(n):
    for i in range(2, n+1):
        if n%i == 0:
            n=n//i
            print(i)
            break
    if n > 1:
        factorization(n)
    else:
        return 0

factorization(int(input()))
