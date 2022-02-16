import sys
# input
N = int(input())
answer = N
for _ in range(N):
    follow = ''
    word = list(sys.stdin.readline().strip())
    check = set()
    for i in range(len(word)):
        back = word.pop()
        if back == follow:
            continue
        elif back not in check:
            check.add(back)
        else:
            answer -= 1
            break
        follow = back
print(answer)
