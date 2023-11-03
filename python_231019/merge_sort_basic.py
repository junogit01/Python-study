nums = [int(x) for x in input().split()]

def merge_sort(nums):
    length = len(nums)
    
    # 분할
    if length <= 1:
        return nums
    mid = length // 2
    group1 = merge_sort(nums[:mid])
    group2 = merge_sort(nums[mid:])
    
    sorted_nums = []
    
    # 합병
    while group1 and group2:
        if group1[0] < group2[0]:
            sorted_nums.append(group1.pop(0))
        else:
            sorted_nums.append(group2.pop(0))
    while group1:
        sorted_nums.append(group1.pop(0))
    while group2:
        sorted_nums.append(group2.pop(0))
    return sorted_nums

print(merge_sort(nums))