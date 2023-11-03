import sys
from collections import deque

k = int(sys.stdin.readline())

nums = deque()

for i in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        nums.append(num)
    else:
        nums.pop()

print(sum(nums))