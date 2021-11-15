stack = []
for i in range(int(input())):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))