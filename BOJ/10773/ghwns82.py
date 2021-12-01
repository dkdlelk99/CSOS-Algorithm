# 10773
result = []

for _ in range(int(input())):
    if (n:= int(input()))==0:
        result.pop()
    else:
        result.append(n)
print(sum(result))
