loop = input()
while loop:
    ans = "yes" if str(loop) == str(loop)[::-1] else "no"
    print(ans)
    loop = int(input())
