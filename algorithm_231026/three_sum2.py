def three_sum(nums: list[int]) -> list[list[int]]:
    result = [] 
    nums.sort()
    
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: continue # 중복된 원소는 반복문 통과 (단, 첫번째 중복은 허용)
        
        for j in range(i+1, len(nums)-1): 
            if j > i + 1 and nums[j] == nums[j-1]:  continue # 중복된 원소는 반복문 통과 (단, 첫번째 중복은 허용)
            
            for k in range(j+1, len(nums)):                
                if k > j + 1 and nums[k] == nums[k-1]:  continue # 중복된 원소는 반복문 통과 (단, 첫번째 중복은 허용)
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    return result

nums = [-4, 0, 1, -1, 2, 1]
print(three_sum(nums))