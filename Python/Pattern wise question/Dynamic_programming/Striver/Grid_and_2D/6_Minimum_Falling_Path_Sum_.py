"""

Given an n x n array of integers matrix,
 return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses
 the element in the next row that is either directly below or diagonally left/right.
  Specifically,
   the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.


Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100


"""

""" Recursion """

class Solution:
    def solve(self , row , col , matrix , n):
        if  col < 0 or col >=n:
            return float("inf")
        if row == 0:
            return matrix[0][col]
        up = self.solve(row-1 , col , matrix , n) + matrix[row][col]
        left_D = self.solve(row-1 , col-1 , matrix , n)+ matrix[row][col]
        right_D = self.solve(row-1 , col+1 , matrix , n)+ matrix[row][col]
        return min(up , min(left_D , right_D))


    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        mini = float("inf")
        for col in range(n):
            f = self.solve(m-1 , col , matrix , n)
            mini = min(mini , f)
        return mini

""" Top - Down """

class Solution:
    def solve(self , row , col , matrix , n , memo):
        if  col < 0 or col >=n:
            return float("inf")
        if row == 0:
            return matrix[0][col]
        if memo[row][col] != -1:
            return memo[row][col]
        up = self.solve(row-1 , col , matrix , n , memo) + matrix[row][col]
        left_D = self.solve(row-1 , col-1 , matrix , n , memo)+ matrix[row][col]
        right_D = self.solve(row-1 , col+1 , matrix , n , memo)+ matrix[row][col]
        memo[row][col] =  min(up , min(left_D , right_D))
        return memo[row][col]


    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = [[-1 for i in range(n)] for j in range(m)]
        mini = float("inf")
        for col in range(n):
            f = self.solve(m-1 , col , matrix , n  , memo)
            mini = min(mini , f)
        return mini



""" Bottom - up """

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[0][i] = matrix[0][i]
        for i in range(1 , m):
            for j in range(n):
                up = dp[i-1][j] + matrix[i][j]
                if j > 0:
                    left_D = dp[i-1][j-1] + matrix[i][j]
                else:
                    left_D  = float("inf") + matrix[i][j]
                if j < n-1:
                    right_D = dp[i-1][j+1] + matrix[i][j]
                else:
                    right_D = float("inf") + matrix[i][j]
                dp[i][j] = min(up , min(left_D , right_D))

        mini = float("inf")

        for col in range(n):
            f = dp[m-1][col]
            mini = min(mini , f)
        return mini
