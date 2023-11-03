import sys

num = int(input())
nums = [int(sys.stdin.readline()) for _ in range(num)]

def selection_sort(nums) :
    length = len(nums)
    for x in range(length - 1) :
        min = x
        for y in range(x + 1, length) :
            if nums[min] > nums[y] :
                min = y
        nums[x], nums[min] = nums[min], nums[x]
    return nums

def insertion_sort(nums):
    length = len(nums)
    for x in range(1, length):
        key = nums[x]
        y = x - 1
        while y >= 0 and nums[y] > key:
            nums[y + 1] = nums[y]
            y -= 1
        nums[y + 1] = key
    return nums

def merge_sort(nums):
    length = len(nums)
    
    # 분할
    if length <= 1:
        return nums
    mid = length // 2
    group1, group2 = nums[:mid], nums[mid:]
    merge_sort(group1)
    merge_sort(group2)
    
    idx, idx1, idx2 = 0, 0, 0
    
    # 합병
    while idx1 < len(group1) and idx2 < len(group2):
        if group1[idx1] < group2[idx2]:
            nums[idx] = group1[idx1]
            idx1 += 1
            idx += 1
        else:
            nums[idx] = group2[idx2]
            idx2 += 1
            idx += 1
    while idx1 < len(group1):
        nums[idx] = group1[idx1]
        idx1 += 1
        idx += 1
    while idx2 < len(group2):
        nums[idx] = group2[idx2]
        idx2 += 1
        idx += 1
    return nums

# for i in selection_sort(nums):
#     print(i)

# for i in insertion_sort(nums):
#     print(i)

# for i in merge_sort(nums):
#     print(i)

nums.sort()
for i in nums:
    print(i)