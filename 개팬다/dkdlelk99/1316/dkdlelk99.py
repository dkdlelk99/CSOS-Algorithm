import sys
# input
N = int(sys.stdin.readline())
answer = 0
for i in range(N):
    letter = set()
    line = list(sys.stdin.readline().strip())
    loop = len(line)
    for i in range(loop - 1):
        vs = line.pop()

        if vs == line[-1]:
            continue
        elif vs not in letter:
            letter.add(vs)
        elif vs in letter:
            break

        if i == loop-2:
            answer += 1


print(answer)
