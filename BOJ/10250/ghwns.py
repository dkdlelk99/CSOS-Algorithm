for _ in range(int(input())):
    H,W,N=map(int, input().split())
    floor = [str(i) for i in range(1, H+1)]
    print(floor[N%H-1]+ str((N-1)//H+1).zfill(2))
