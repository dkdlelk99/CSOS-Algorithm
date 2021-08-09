n=int(input())
n_list=list(map(int,input().split())) #A배열의 원소
n_list=sorted(n_list) #A배열 원소 정렬
m=int(input())
m_list=list(map(int,input().split()))

def binary_search(arr, start, end): #이분 탐색
    if(start>end):
        return False
    mid=(start+end)//2
    if(arr==n_list[mid]):
        return True
    elif(arr<n_list[mid]):
        return binary_search(arr, start, mid-1)
    else:
        return binary_search(arr, mid+1, end)

for i in m_list:
    output=binary_search(i,0,n-1)
    if(output==False):
        print(0)
    else:
        print(1)

