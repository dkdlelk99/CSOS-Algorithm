import sys, heapq
# input
T = int(sys.stdin.readline())
min_heap = []
max_heap = []

for _ in range(T):
    for i in range(int(sys.stdin.readline())):
        cmd = sys.stdin.readline().strip()
        if cmd[0] == 'I':
            val = int(cmd[1:])
            if val > 0:
                heapq.heappush(max_heap, val)
            else:
                heapq.heappush(min_heap, val)
        elif cmd == "D 1":
            if len(max_heap) != 0:
                heapq.heappop(max_heap)
            elif len(max_heap) == 0 and len(min_heap) != 0:
                heapq.heappop(min_heap)
        elif cmd == "D -1":
            if len(min_heap) != 0:
                heapq.heappop(min_heap)
            elif len(min_heap) == 0 and len(max_heap) != 0:
                heapq.heappop(max_heap)
    if len(min_heap) == 0 and len(max_heap) == 0:
        print("EMPTY")
    else:
        print(max(max(min_heap), max(max_heap)), min(min(min_heap), min(max_heap)))