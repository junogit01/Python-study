def two_sum(nums, target) -> list[int]:
    # 투 포인터 기법을 이용해 개선한 방식
    # (현재 풀이에는 적합하지 않다. -> 정렬된 nums만 들어오는 것이 아니기 때문!)
    
    # lt, rt는 위치값
    lt = 0
    rt = len(nums) - 1
    
    nums.sort()
    while lt < rt:
        sum = nums[lt] + nums[rt]
        if sum < target:
            lt += 1
        elif sum > target:
            rt -= 1
        else:
            return [lt, rt]

nums = [2, 5, 11, 15]
target = 6

print(two_sum(nums, target))