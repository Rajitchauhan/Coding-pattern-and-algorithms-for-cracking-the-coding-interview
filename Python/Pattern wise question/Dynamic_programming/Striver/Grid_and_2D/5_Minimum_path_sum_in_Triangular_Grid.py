"""

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally,
 if you are on index i on the current row,
 you may move to either index i or index i + 1 on the next row.



Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10


Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104

"""

""" Recursion """
class Solution:
    def solve(self , i  , j, triangle , n):
        if i==n:
            return triangle[i][j]
        if i > n or  j > n:
            return float("inf")
        down = self.solve(i+1 , j , triangle , n)
        daiogalLeft = self.solve(i+1 , j+1 , triangle , n)
        return min(down , daiogalLeft) + triangle[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.solve(0 , 0, triangle , len(triangle)-1)

""" top - down """
class Solution:
    def solve(self , i  , j, triangle , n , memo):
        if i==n:
            return triangle[i][j]
        if i > n or  j > n:
            return float("inf")
        if memo[i][j] != -1:
            return memo[i][j]
        down = self.solve(i+1 , j , triangle , n , memo)
        daiogalLeft = self.solve(i+1 , j+1 , triangle , n , memo)
        memo[i][j] =  min(down , daiogalLeft) + triangle[i][j]
        return memo[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        memo = [[-1 for  j in range(m)]  for i in  range(m)]
        return self.solve(0 , 0, triangle , len(triangle)-1 , memo)
