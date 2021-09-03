def prime(n):
    if n ==1:
        return 0
    
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return 0
    return n

a = [i for i in range(int(input()), int(input())+1) if prime(i)]
if len(a):
    print(sum(a), a[0])
else:
    print(-1)
