# 9012
# 성공

for _ in range(int(input())):
    temp = []
    for i in input():
        if i =="(":
            temp.append(i)
        elif i == ")" and not temp:
            temp.append(i)
            break
        else:
            temp.pop()
    if temp:
        print("NO")
    else:
        print("YES")
