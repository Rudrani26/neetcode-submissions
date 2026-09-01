class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[m-1][n-1] = grid[m-1][n-1]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = grid[i][j]
                else:
                    down = dp[i+1][j] if i + 1 < m else float("inf")
                    right = dp[i][j+1] if j + 1 < n else float("inf")
                
                    dp[i][j] = grid[i][j] + min(down, right)

        return dp[0][0]
        