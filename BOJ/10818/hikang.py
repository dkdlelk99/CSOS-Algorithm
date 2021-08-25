from sys import stdin

N = int(stdin.readline())

array = list(map(int,stdin.readline().split()))
print(min(array), max(array)) 