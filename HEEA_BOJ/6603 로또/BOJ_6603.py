def func(k, index, l):
    if(k==6):
        for i in range(6):
            print(arr[i], end=" ")
        print("")
        return #arr[k]=l[i]를 둔 상태에서 func(k+1, i+1, l)에 들어갔다가 모든 과정을 끝내서 되돌아 가야함
    for i in range(index,l[0]+1): #index 값도 넘겨 주어 이전 index는 사용 안함
        if(isused[l[i]]==False):
            arr[k]=l[i]
            isused[l[i]]=True
            func(k+1, i+1, l) #return을 통해 되돌아 오는 자리
            isused[l[i]]=False #isused[l[i]]의 값을 False로 하여 수 i가 사용되고 있지 않음을 명시하고 있는데 arr[k]의 값은 0으로 돌리지 않음 => 어차피 다른 수로 덮어쓸 거기 때문
    return #for문이 끝나고 되돌아감

while True:
    l=list(map(int,input().split()))
    if(l[0]==0):
        break
    arr=[0]*6
    isused=[False]*50
    func(0, 1, l)
    print("")
