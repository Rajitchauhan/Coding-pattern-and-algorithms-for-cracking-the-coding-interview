"""
There is a robot on an m x n grid.
 The robot is initially located at the top-left corner
  (i.e., grid[0][0]).
  The robot tries to move to the bottom-right corner
   (i.e., grid[m - 1][n - 1]).
   The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that
the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:
1 <= m, n <= 100


"""
""" Recursion TC : expon SC : O(N) """
class Solution:
    def solve(self, m, n):
        if m==0 and n==0:
            return 1
        if m < 0 or n < 0:
            return 0
        up = self.solve(m-1 , n)
        left = self.solve(m, n-1)
        return left + up
    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve(m-1 , n-1)


""" Top- Down """
class Solution:
    def solve(self, m, n , memo):
        if m==0 and n==0:
            return 1
        if m < 0 or n < 0:
            return 0
        if memo[m][n]  != -1:
            return  memo[m][n]
        up = self.solve(m-1 , n , memo)
        left = self.solve(m, n-1 , memo)
        memo[m][n] = left + up
        return memo[m][n]
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)]  for i in range(m) ]
        return self.solve(m-1 , n-1 , memo)


""" Bottom up """
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)]  for i in range(m) ]
        dp[0][0] =  1 """ we can comments this  , this will no effect program`s output """
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j] = 1
                else:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i-1][j]  + dp[i][j-1]
        return dp[m-1][n-1]

""" space optimization TC : O(n^2) SC : O(N) """
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp = [[0 for _ in range(n)]   for i in range(m) ]
        pre = [0]*n
        curr = [0]*n
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    curr[j] = 1
                else:
                    if i > 0 and j > 0:
                        curr[j] = pre[j]  + curr[j-1]
            pre = curr
        return pre[n-1
