n,c=map(int,input().split())
l=[]

for i in range(n):
    l.append(int(input()))

l=sorted(l)
minlen=1 #최소 길이
maxlen=l[n-1]-l[0] #최대 길이
result=0

while(minlen<=maxlen):
    mid=(minlen+maxlen)//2
    start=l[0] #설치 시작점
    count=1 #설치 개수, 시작점에 이미 1개를 설치했으므로 초기값은 항상 1
    for i in l:
        dis=i-start #새로 설치할 공유기까지의 거리
        if(dis>=mid): #새로 설치할 공유기는 가장 가까운 거리의 길이보다는 크거나 같아야 설치 가능
            count+=1
            start=i
    if(count>=c): #설치한 공유기의 개수가 크거나 같을 경우 최소 길이를 올려준다
        minlen=mid+1
        result=mid
    else:
        maxlen=mid-1

print(result)