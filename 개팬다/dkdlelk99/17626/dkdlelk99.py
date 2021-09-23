n = int(input())

answer = 0
while n != 0:
    temp = 1
    while n - temp**2 >= 0:
        temp += 1
    n -= (temp-1)**2
    answer += 1
print(answer)