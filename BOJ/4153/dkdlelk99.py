# 직각 삼각형 확인
condition = True
while condition:
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    a,b,c = a**2, b**2, c**2

    print("right" if a+b == c or b+c == a or a+c == b else "wrong")
    # if a+b == c or b+c == a or a+c == b:
    #     print("right")
    # else:
    #     print("wrong")