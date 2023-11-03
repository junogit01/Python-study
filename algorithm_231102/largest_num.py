nums = [999999991,9]

def largest_number(nums: list[int]) -> str:
    nums = [str(i) for i in nums]
    print(nums)
    # 문자열을 곱해서 정렬해야 [30, 3] 정렬된다.
    nums.sort(key=lambda x: x*9, reverse=True)
    
    # result = ''
    # for i in nums:
    #     result += i
    # return str(int(result))
    
    return str(int(''.join(nums)))
    
print(largest_number(nums))