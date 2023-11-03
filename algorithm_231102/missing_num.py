nums = [0, 3, 1]

# 1484ms
# nums를 (n+1)번 반복한다.
# 각각의 요소가 nums에 있는지 체크!
# def missing_number(nums: list[int]) -> int:
#     for i in range(0, len(nums)+1):
#         if i not in nums:
#             return i
# print(missing_number(nums))

# 122ms
# 0~n까지의 합계를 구한다 (total)
# nums 배열의 합계를 구한다 (nums_sum)
# total - nums_sum의 결과를 반환
# def missing_number(nums: list[int]) -> int:
#     n = len(nums)
#     total = n * (n + 1) // 2
#     nums_sum = sum(nums)
#     return total - nums_sum
# print(missing_number(nums))

# 129ms
# nums를 정렬하면, 0부터 n까지 정렬된다.
# 인덱스와 값이 일치하지 않으면 반환하고, 모두가 일치하면 전체 크기(최대값)을 반환
def missing_number(nums: list[int]) -> int:
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)

print(missing_number(nums))