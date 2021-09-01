def prime (n):
    if n ==1:
        return 0
    
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

input()
print(sum([prime(int(i)) for i in input().split()]))
