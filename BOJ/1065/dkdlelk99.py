N = input()
answer = 99
if int(N) < 100:
    print(N)
else:
    for i in range(100, int(N)+1):
        f, s, t = int(str(i)[0]), int(str(i)[1]), int(str(i)[2])
        if f-s == s-t:
            answer += 1
    print(answer)
