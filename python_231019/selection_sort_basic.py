nums = [int(i) for i in input().split()]

def selection_sort(nums):
    def find_min_idx():
        length = len(nums)
        min_idx = 0
        for i in range(1, length):
            if nums[min_idx] > nums[i]:
                min_idx = i
        return min_idx
    
    sorted_nums = []
    while nums:
        min_idx = find_min_idx()
        sorted_nums.append(nums.pop(min_idx))
    return sorted_nums

print(selection_sort(nums))