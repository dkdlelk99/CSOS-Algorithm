n = input()
result=0
check=0
check6=False
check9=False

for i in n:
    if(i=='6' and check6==False):
        check+=n.count(i)
        check6=True
    elif(i=='9' and check9==False):
        check+=n.count(i)
        check9=True
    elif(i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='7' or i=='8'):
        if(result<n.count(i)):
            result=n.count(i)

if(result>round(check/2)):
    print(result)
else:
    print(round(check/2))