"""

Given a m x n grid filled with non-negative numbers,
 find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

"""

""" Top - down """

class Solution:
    def solve(self , m, n, grid , memo):
        if m==0 and n==0:
            return grid[0][0]
        if m < 0 or n < 0:
            return float("inf")
        if memo[m][n]  != -1:
            return memo[m][n]
        left = self.solve(m, n-1 , grid , memo) + grid[m][n]
        up = self.solve(m-1, n , grid , memo) + grid[m][n]
        memo[m][n] =  min(left , up)
        return memo[m][n]
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[-1 for _ in range(n)] for i in range(m)]
        return self.solve(m-1 ,  n-1 , grid , memo)

""" Bottom up """

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = grid[0][0]
                else:
                    up= grid[i][j]
                    if i > 0:
                        up += dp[i-1][j]
                    else:
                        up += float("inf")
                    left = grid[i][j]
                    if j > 0:
                        left += dp[i][j-1]
                    else:
                        left += float("inf")
                    dp[i][j] = min(left , up)
        return dp[m-1][n-1]
