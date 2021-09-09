import sys

while True:
    n=int(sys.stdin.readline())
    if(n!=0):
        n_bin=format(n-1,'b') #2진수로 변환해주는 함수 bin()의 경우 접두어 #0b가 붙기 때문에 접두어를 제외한 수를 사용해야 하므로 foramt을 사용해서 제거하기
        n_bin="".join(reversed(n_bin))
        result=[]
        start=0
        for i in n_bin:
            if(i=='0'):
                start+=1
            else:
                result.append(3**start)
                start+=1
        if(len(result)==0):
            print("{ }")
        else:
            print("{ ", end="")
            for i in range(len(result)-1):
                print(str(result[i])+", ",end="")
            print(str(result[len(result)-1])+" }")
    else:
        break
    