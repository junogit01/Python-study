import heapq
heap = []

heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
heapq.heappush(heap, 9)
heapq.heappush(heap, 4)

print(heap)

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))