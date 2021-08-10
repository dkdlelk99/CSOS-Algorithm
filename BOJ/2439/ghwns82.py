import sys
a = int(sys.stdin.readline())
for i in range(1, a+1):
    print(" "*(a-i)+ "*" * (i))

# walrus 사용
for i in range(1, a := int(sys.stdin.readline())+1):
    print(" "*(a-i)+ "*" * (i))

    
# 한줄코드 불가
