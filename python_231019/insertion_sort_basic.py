nums = [int(i) for i in input().split()]

def insertion_sort(nums):
    def find_insert_idx():
        length = len(sort_nums)
        for i in range(length):
            if number < sort_nums[i] :
                return i
        return length
        
    sort_nums = []
    while nums:
        number = nums.pop(0)
        insert_idx = find_insert_idx()
        sort_nums.insert(insert_idx, number)
    return sort_nums

print(insertion_sort(nums))