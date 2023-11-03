# 방법 1) itertools 모듈의 product를 사용
# import sys
# import itertools

# n, m = [int(i) for i in sys.stdin.readline().split()]
# nums = [i for i in range(1, n + 1)]

# results = list(itertools.product(nums, repeat=m))
# for i in results:
#     print(" ".join(map(str, i)))

# 방법 2) 재귀 _ index 사용
# import sys
# n, m = [int(i) for i in sys.stdin.readline().split()]
# nums = [i for i in range(1, n + 1)] # [1, 2, 3]
# results = [0] * m

# def dfs(idx):
#     if idx >= m:
#         print(*results)
#         return
#     for i in range(n):
#         results[idx] = nums[i]
#         dfs(idx + 1)
# dfs(0)

# 방법 3) 재귀 _ path 사용
# import sys
# n, m = [int(i) for i in sys.stdin.readline().split()]
# nums = [i for i in range(1, n + 1)] # [1, 2, 3]

# def dfs(nums, path):
#     if len(path) == m :
#         print(*path)
#         return
#     for i in range(n):
#         dfs(nums, path + [nums[i]])

# dfs(nums, [])

# 방법 4) 재귀 _ ( )
import sys
n, m = [int(i) for i in sys.stdin.readline().split()]
stack = []

def dfs():
    if len(stack) == m:
        print(*stack)
        return
    for i in range(1, n + 1):
        stack.append(i)
        dfs()
        stack.pop()

dfs()