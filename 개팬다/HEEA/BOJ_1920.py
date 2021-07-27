n=int(input())
n_list=list(map(int,input().split())) #A 배열의 원소
a=[0]*(max(n_list)+1) #A 배열
m=int(input())
m_list=list(map(int,input().split()))
result=[]

for i in n_list:
    a[i]=1

for i in m_list:
    if(i>len(a)):
        result.append(0)
    elif(a[i]==1):
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)

