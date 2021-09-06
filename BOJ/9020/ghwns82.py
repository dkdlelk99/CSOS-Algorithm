def prime(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    N = int(input())
    for i in range(2, N//2+1)[::-1]:
        if prime(i) and prime(N-i):
            print(i, N-i)
            break
