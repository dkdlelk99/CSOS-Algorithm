# 방법 1
for i in range(int(input())):
    txt = ""
    a = input().split()
    for i in a[1]:
        txt += i*int(a[0])
    print(txt)
    
# 방법 2
# # join의 사용
# for i in range(int(input())):
#     a = input().split()
#     print(''.join([d*int(a[0])for d in a[1]]))
