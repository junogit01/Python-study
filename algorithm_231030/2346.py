import sys
from collections import deque

n = int(sys.stdin.readline())
balloon = deque(enumerate([int(i) for i in sys.stdin.readline().split()]))

result = []
while balloon:
    index, move = balloon.popleft()
    result.append(index + 1)
    if move > 0:
        balloon.rotate(-(move - 1))
    else:
        balloon.rotate(-move)
        
print(' '.join(map(str, result)))