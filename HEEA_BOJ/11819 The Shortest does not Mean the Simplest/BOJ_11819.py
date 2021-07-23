a,b,c=map(int,input().split())

b_bin=format(b,'b')
b_bin="".join(reversed(b_bin))
result=1

for i in b_bin:
    if(i=='1'):
        result=int(a*result%c)
    a=int(pow(a,2)%c)
print(result)