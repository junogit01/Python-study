# nums = []
# for i in range(9) :
#     num = int(input())
#     nums.append(num)
nums = [int(input()) for _ in range(9)]

# max_num = nums[0]
# index = 0
# for i in range(1, len(nums)):
#     if max_num < nums[i]:
#         max_num = nums[i]
#         index = i + 1
max_num = max(nums)
index = nums.index(max_num) + 1 

print(max_num, index)