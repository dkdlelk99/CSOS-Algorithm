import sys, heapq
# input
N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if n > 0: # 자연수 일 때
        heapq.heappush(heap, -n) # 파이썬이 제공하는 heapq는 최소 힙이다. 그래서 -를 붙여서 최대 힙으로 사용
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))