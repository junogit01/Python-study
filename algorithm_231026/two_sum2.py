def two_sum(nums, target) -> list[int]:
    # 1차 개선된 방식
    for i, n in enumerate(nums): # nums의 0번째 2
        gap = target - n # gap = 7
        if gap in nums[i+1:]: # nums의 1번째부터 끝까지에서 7을 탐색
            return [i, nums[i+1:].index(gap) + (i + 1)]

nums = [2, 7, 11, 15]
target = 9