import sys
import heapq

n=int(sys.stdin.readline())
heap=[]

for _ in range(n):
    x=int(sys.stdin.readline())
    if(x==0):
        if(len(heap)==0):
            print(0)
        else:
            print(heap[0][1])
            heapq.heappop(heap)
    else:
        heapq.heappush(heap, (abs(x), x))
