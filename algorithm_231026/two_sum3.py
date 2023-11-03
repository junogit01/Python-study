def two_sum(nums, target) -> list[int]:
    # 2차 개선된 방식
    d_nums = {}
    for i, n in enumerate(nums):
        d_nums[n] = i

    for i, n in enumerate(nums):
        gap = target -n # gap = 7
        if gap in d_nums and i != d_nums[gap]:
            return [i, d_nums[gap]]       