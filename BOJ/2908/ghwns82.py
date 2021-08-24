#풀이 1

num1, num2 = input().split()
print(max(
    int(num1[::-1]),
    int(num2[::-1])
))


# 풀이 2
#print(max(*map(int, input()[::-1].split())))
