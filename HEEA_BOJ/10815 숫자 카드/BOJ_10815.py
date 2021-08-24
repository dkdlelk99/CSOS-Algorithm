n=int(input())
n_list=list(map(int,input().split()))
n_list=sorted(n_list)

m=int(input())
m_list=list(map(int,input().split()))
result=[]

def binary_search(arr, start, end):
    while (start<=end):
        mid=(start+end)//2
        if(arr==n_list[mid]):
            return 1
        elif(arr>n_list[mid]):
            start=mid+1
        else:
            end=mid-1
    return 0

for i in m_list:
    result.append(binary_search(i, 0, n-1))

for i in result:
    print(i, end=" ")
