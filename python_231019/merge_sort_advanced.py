nums = [int(x) for x in input().split()]

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

print(merge_sort(nums))