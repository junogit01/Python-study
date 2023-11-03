def three_sum(nums: list[int]) -> list[list[int]]:
    result = [] 
    nums.sort() # [-4, -1, -1, 0, 1, 2]
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: continue # 중복된 원소는 반복문 통과 (단, 첫번째 중복은 허용)
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                right -= 1
                left += 1
    return result

nums = [-4, 0, 1, -1, 2, -1]
print(three_sum(nums))