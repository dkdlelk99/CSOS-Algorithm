import heapq #파이썬의 힙 모듈은 최소를 기준으로 이루어짐. 따라서, 음수의 경우는 숫자가 클수록 더 작기때문에 이를 이용하여 튜플의 인덱스로 음수값을 사용하여 힙 모듈을 사용하면 됨
import sys

n=int(sys.stdin.readline())
heap=[]

for i in range(n):
    x=int(sys.stdin.readline())
    if(x==0):
        if(len(heap)==0):
            print(0)
        else:
            print(heap[0][1])
            heapq.heappop(heap)
    else:
        heapq.heappush(heap, (-x,x))