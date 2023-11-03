import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, -1 * x)
    else:
        if len(heap) != 0:
            print(-1 * heapq.heappop(heap))
        else :
            print(0)