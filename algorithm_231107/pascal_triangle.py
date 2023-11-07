class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        dptable = [[0] *(i+1) for i in range(numRows)]
        for i in range(numRows):
            dptable[i][0] = 1
            dptable[i][-1] = 1
        for i in range(2, numRows): # 행(가로줄)
            for j in range(1, j): # 열(세로줄)
                dptable[i][j] = dptable[i-1][j-1] + dptable[i-1][j]
        return dptable
                

print(Solution().generate(5))