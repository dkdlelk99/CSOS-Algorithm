n=int(input())
arr=[]
cnt=0
isused1=[False]*n #수직
isused2=[False]*(2*(n-1)+1) #오른쪽 대각선
isused3=[False]*(2*(n-1)+1) #왼쪽 대각선

def func(current): #current는 x로 생각하기
    global cnt
    if(current==n):
        cnt+=1
        return
    for i in range(n): #i는 y로 생각하기
        if(isused1[i]==True or isused2[current+i]==True or isused3[(current-i)+(n-1)]==True): #왼쪽 대각선의 경우 음수가 나오므로(인덱스는 음수가 없음) n-1을 해서 양수로 만듬
            continue #하나라도 True가 존재하면 다음 i로 넘어가기
        isused1[i]=True
        isused2[current+i]=True
        isused3[(current-i)+(n-1)]=True
        func(current+1)
        isused1[i]=False
        isused2[current+i]=False
        isused3[current-i+(n-1)]=False

func(0)
print(cnt)
