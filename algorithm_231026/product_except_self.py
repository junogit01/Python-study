nums = [1, 2, 3, 4]

def product_except_self(nums:list[int]) -> list[int]:
    # 1단계
    # result = [1, 1, 1, 1] 
    # nums 배열의 길이만큼 1로 채운 리스트를 생성
    result = [1] * len(nums) # result = [1 for _ in nums]
    
    # 2단계
    # 0번째부터 2번째까지 반복 nums = [1, 2, 3, 4]
        # p = 0번째
        # result[1] *= p
        # p = 0번째 * 1번째
        # result[2] *= p
        # p = 0번째 * 1번째 * 2번째
        # result[3] *= p
    num = 1
    for i in range(0, len(nums)-1):
        num *= nums[i]
        result[i+1] *= num
    
    # 3단계
    # 3번째부터 1번째까지 반복
        # p = 3번째
        # result[2] *= p
        # p = 3번째 * 2번째
        # result[1] *= p
        # p = 3번째 * 2번째 * 1번째
        # result[0] *= p
    num = 1
    for i in range(len(nums)-1, 0, -1):
        num *= nums[i]
        result[i-1] *= num
    
    print(result)
    return result

product_except_self(nums)


# def product_except_self(nums:list[int]) -> list[int]:
#     result = []

#     num = 1
#     for i in range(len(nums)): # nums = [1, 2, 3, 4]
#         # print(f'1 현재 result = {result}')
#         # print(f'2 i는 {i}입니다. result에 {num}을 추가합니다.')
#         result.append(num)
#         # print(f'3 추가된 result = {result}')
#         num *= nums[i]
#         # print(f'4 num에 {nums[i]}를 곱합니다.')

#     num = 1
#     for i in range(len(nums)-1, -1, -1):
#         result[i] *= num
#         num *= nums[i]

#     return result