while(True):
    A,B = map(int,input().split())

    # 마지막 입력으로 0 0 이 들어오면 break
    if(A==0 and B==0):
        break
    else:
        print(A+B)