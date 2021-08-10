import sys

a = int(sys.stdin.readline())
for i in range(a):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {A} + {B} = {A+B}')
    
    
# 한줄코딩
# [print(f'Case #{i+1}: {j[0]} + {j[1]} = {j[0] + j[1]}') for i in range(int(sys.stdin.readline())) for j in [list(map(int, sys.stdin.readline().split()))]]
