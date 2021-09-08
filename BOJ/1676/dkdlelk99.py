five = 0
for i in range(1, int(input())+1):
    checkpoint = i
    while checkpoint % 5 == 0: # 5의 배수를 만나면 해당 수에 5가 몇번 곱해졌는지 카운팅
        five += 1
        checkpoint //= 5
print(five)