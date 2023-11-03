nums = [1, 2, 3]
def subsets(nums):
    subset_result = []
    subset = []
    idx = 0
    def dfs(idx, subset):
        subset_result.append(subset)
        for i in range(idx, len(nums)):
            new_subset = subset[:]
            new_subset.append(nums[i])
            dfs(i+1, new_subset)
    dfs(idx, subset)
    return subset_result

print(subsets(nums))