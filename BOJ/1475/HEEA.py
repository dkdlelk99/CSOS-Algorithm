import sys

n = sys.stdin.readline()
n = n.replace("6","9")
result=0

for i in n:
    if(i=='9'):
        if(n.count(i)%2==0):
            if(result<n.count(i)//2):
                result=n.count(i)//2
        else:
            if(result<(n.count(i)//2+1)):
                result=n.count(i)//2+1
    else:
        if(result<n.count(i)):
            result=n.count(i)

print(result)

