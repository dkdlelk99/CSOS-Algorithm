import sys

input = sys.stdin.readline

n, m = map(int, input().split())

p_dict = {}

for i in range(n):
    p_dict[(name:=input().rstrip())] = i+1
    p_dict[i+1] = name

for _ in range(m):
    if (quiz:=input().rstrip()).isalpha():
        print(p_dict[quiz])
    else:
        print(p_dict[int(quiz)])
