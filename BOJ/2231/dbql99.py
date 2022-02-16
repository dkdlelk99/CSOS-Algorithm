target = int(input())

for i in range(target):
    num = sum(map(int, str(i)))
    temp = num + i
    if temp == target:
        print(i)
        break    #여기서부터 어떻게 하느냐에 따라 출력물이 매우 달랐다. 이 점을 유위하고 다시 복습하도록 하자. 
else:
    print("0")
