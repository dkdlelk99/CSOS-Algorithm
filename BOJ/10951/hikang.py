import sys

while(True):
    try:
        A,B = map(int,sys.stdin.readline().split())
    except:
        break
    print(A+B)
