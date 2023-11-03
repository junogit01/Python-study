nums = [1, 2, 3]
def permute(nums):
    permutations = []
    pmt = []
    # 입력데이터 : [1, 2, 3] 반복
    def dfs(nums):
        # 입력데이터 [] -> 순열들.append(순열)
        if len(nums) == 0:
            permutations.append(pmt.copy()) # copy
            return permutations # 끝나는 부분에서 반드시 return!!!
        for i in nums:
            pmt.append(i)
            new_nums = nums.copy() # copy
            new_nums.remove(i)
            dfs(new_nums)
            pmt.pop() # 반드시 하나씩 빼주기!!
    dfs(nums)
    return permutations

print(permute(nums))