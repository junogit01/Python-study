nums = [int(i) for i in input().split()]

def insertion_sort(nums):
    length = len(nums)
    for x in range(1, length):
        key = nums[x]
        print(f"KEY는 {x}번째 값인 {key}이다.")
        y = x - 1
        while y >= 0 and nums[y] > key:
            print(f"\t Y번째 값{nums[y]}과 x번째 값{key} 비교")
            nums[y + 1] = nums[y]
            y -= 1
        nums[y + 1] = key
    return nums

print(insertion_sort(nums))