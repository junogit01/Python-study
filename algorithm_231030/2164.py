# import sys
# n = int(sys.stdin.readline())

# queue = [i for i in range(1, n + 1)]

# while len(queue) > 1:
#     queue.pop(0)
#     queue.append(queue.pop(0))
    
# print(queue[0])
# print(queue.pop())
# print(*queue)

import sys
from collections import deque
n = int(sys.stdin.readline())

queue = deque([i for i in range(1, n + 1)])

while len(queue) > 1:
    queue.popleft()
    print(queue)
    queue.append(queue.popleft()) # queue.rotate(-1)
    print(queue)
    
print(queue.pop())