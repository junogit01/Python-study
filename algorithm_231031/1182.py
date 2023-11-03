import sys

n, s = [int(i) for i in sys.stdin.readline().split()]
nums = [int(i) for i in sys.stdin.readline().split()]

result = 0

def dfs(idx, sum):
    global result
    if idx >= n:
        return
    sum = sum + nums[idx]
    if sum == s:
        result += 1
    dfs(idx+1, sum)
    dfs(idx+1, sum - nums[idx])

dfs(0, 0)
print(result)