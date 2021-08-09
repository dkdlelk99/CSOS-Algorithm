n=int(input())
n_list=list(map(int,input().split()))
n_list=sorted(n_list)

m=int(input())
m_list=list(map(int,input().split()))

def binary_search(arr, start, end):
    while(start<=end):
        mid=(start+end)//2
        if(arr==n_list[mid]):
            return True
        elif(arr>n_list[mid]):
            return binary_search(arr, mid+1, end)
        else:
            return binary_search(arr, start, mid-1)
    return False

for i in m_list:
    result=binary_search(i, 0, n-1)
    if(result==True):
        print(1)
    else:
        print(0)
