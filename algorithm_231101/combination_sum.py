candidates = [2, 3, 6, 7]
target = 7

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    combination_sums = []
    result = []
    def dfs(target, idx):
        if target < 0:
            return
        if target == 0:
            combination_sums.append(result.copy())
            return
        for i in range(idx ,len(candidates)):
            # if candidates[i] == 0 : continue
            result.append(candidates[i])
            dfs(target-candidates[i], i)
            result.pop()
    dfs(target, 0)
    return combination_sums

print(combination_sum(candidates, target))