# 방법 1
# import sys
# for _ in range(int(sys.stdin.readline())):
#     count= 0
#     for i in (b := list(map(int, sys.stdin.readline().split())))[1:]:
#         if i > (sum(b) - b[0])//(b[0]):
#             count +=1
#     print(f'{count*100/b[0]:.3f}%')


# 방법 2
# unpaking 사용  훨씬 깔끔
for _ in range(int(input())):
    count= 0
    n, *grade = list(map(int, input().split()))
    for i in grade:
        if i > sum(grade)/n:
            count +=1
    print(f'{count*100/n:.3f}%')
