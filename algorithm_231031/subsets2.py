import itertools

nums = [1, 2, 3]
def subsets(nums):
    subset_result = []
    # 0, 1, 2, 3 -> 각 길이에 맞는 조합 가져와서 subset_result에 extend
    for i in range(len(nums)+1):
        subset = [list(i) for i in itertools.combinations(nums, i)]
        subset_result.extend(subset)
    return subset_result

print(subsets(nums))