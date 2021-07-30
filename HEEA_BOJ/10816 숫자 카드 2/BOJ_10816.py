import bisect

n=int(input())
n_list=list(map(int,input().split()))
n_list=sorted(n_list)
print(n_list)
m=int(input())
m_list=list(map(int,input().split()))
c=0

def binary_search(arr, start, end, c):
    if(start>end):
        print(c)
        return True
    mid=(start+end)//2
    if(arr==n_list[mid]):
        c+=1
        binary_search(arr, mid+1, end, c)
    elif(arr>n_list[mid]):
        return binary_search(arr, mid+1, end, c)
    else:
        return binary_search(arr, start, mid-1, c)
print(bisect.bisect_left(n_list,100))
for i in m_list:
    print(bisect.bisect_right(n_list,i)-bisect.bisect_left(n_list,i))
    c=0
