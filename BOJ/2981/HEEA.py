n=int(input())
l=[]
result=[]
output=[]
arr=[]
answer=0

for i in range(n):
    l.append(int(input()))
l=sorted(l)

def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

def cal(k, arr):
    start=2
    while True:
        if(start>k):
            break
        if(k%start==0):
            arr.append(start)
        start+=1

for i in range(1,n):
    result.append(l[i]-l[i-1])

result=sorted(result)
if(len(result)==1):
    answer=result[0]
elif(len(result)==2):
    answer=GCD(result[1],result[0])
else:
    answer=result[0]
    for i in range(1,len(result)):
        answer=GCD(answer,result[i])
    
cal(answer,arr)
for i in arr:
    print(i, end=" ")
