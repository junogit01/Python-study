# 미로 탐색

import sys
from collections import deque

n, m = [int(i) for i in sys.stdin.readline().split()]
maze = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(n)]

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque([[0, 0]])
while queue:
    x, y = queue.popleft()
    for i in direction:
        dx, dy = x+i[0], y+i[1]
        if 0 <= dx < n and 0 <= dy < m:
            if maze[dx][dy] == 1:
                maze[dx][dy] = maze[x][y] + 1
                queue.append([dx, dy])

print(maze[n-1][m-1])