for i in range(int(input())):
    H, W, N = map(int, input().split())
    x, y = N // H+1, N % H
    if y == 0:
        y = H
        x -= 1
    print(y*100 + x)
