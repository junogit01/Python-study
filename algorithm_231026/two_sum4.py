def two_sum(nums, target) -> list[int]:
    # 3차 개선된 방식
    d_nums = {}
    for i, n in enumerate(nums):
        gap = target -n
        if gap in d_nums and i != d_nums[gap]:
            return [i, d_nums[gap]]
        d_nums[n] = i
        
nums = [2, 7, 11, 15]
target = 9