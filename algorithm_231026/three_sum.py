def three_sum(nums: list[int]) -> list[list[int]]:
    result = []
    for i in range(len(nums)-2):        
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    if temp not in result:
                        result.append([nums[i], nums[j], nums[k]])
    return result

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))