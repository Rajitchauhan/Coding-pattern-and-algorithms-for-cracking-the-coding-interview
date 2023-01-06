"""

You are given an m x n integer array grid.
There is a robot initially located at the top-left corner (i.e., grid[0][0]).
 The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]).
  The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid.
 A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1


Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

"""

""" Recursion """
class Solution:
    def solve(self , m , n , grid):
        if(m==0 and n==0):
            return 1
        if(m<0 or n<0):
            return 0
        if(grid[m][n] == 1):
            return 0
        left = self.solve(m , n-1 , grid)
        up = self.solve(m-1 , n , grid)
        return left + up
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m  , n = len(obstacleGrid)  , len(obstacleGrid[0])
        return self.solve(m-1, n-1 , obstacleGrid)

""" Top-Down """
class Solution:
    def solve(self , m , n , grid, memo):
        if(m<0 or n<0):
            return 0
        if(grid[m][n] == 1):
            return 0
        if(m==0 and n==0 ):
            return 1
        if memo[m][n] != -1:
            return memo[m][n]
        up = self.solve(m-1 , n , grid , memo)
        left = self.solve(m , n-1 , grid , memo)
        memo[m][n] =  left + up
        return memo[m][n]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m  , n = len(obstacleGrid)  , len(obstacleGrid[0])
        memo = [[-1 for j in range(n)] for i in range(m)]
        return self.solve(m-1, n-1 , obstacleGrid , memo)

""" Bottom-up """
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m  , n = len(obstacleGrid)  , len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i==0 and j==0:
                    dp[i][j] = 1
                else:
                    if i > 0 or j > 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        


""" space optimization """
