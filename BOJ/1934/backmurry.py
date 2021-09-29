num= int(input())
for i in range(num):
    a,b=map(int,input().split())
    A=a
    B=b
    while B!=0 :
        A=A%B
        temp=B
        B=A
        A=temp
    print(a*b//A)
        
