import sys

N = int(sys.stdin.readline())
a = []

for i in range(N):
    a.append(sys.stdin.readline().strip())

# 중복 제거
a = list(set(a))
# 사전순으로 배치하고 단어 입력시 짧은것 우선
a.sort(key=lambda x:(len(x),x))

for i in a:
    print(i)