import sys, heapq
# input
N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if n > 0: # 자연수 일 때
        heapq.heappush(heap, n)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))