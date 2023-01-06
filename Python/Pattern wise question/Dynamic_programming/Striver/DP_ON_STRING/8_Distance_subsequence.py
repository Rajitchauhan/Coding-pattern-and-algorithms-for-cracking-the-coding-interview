"""

Given two strings s and t, return the number of distinct
subsequences
 of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.



Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag


Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.

"""

class Solution:
    def solve(self , s , t, i , j):
        if j < 0:
            return 1
        if i < 0:
            return 0
        if s[i] == t[j]:
            take = self.solve(s , t, i-1 , j-1)
            move =   self.solve(s , t , i-1 , j)
            return (take + move)
        else:
            return self.solve(s , t, i-1 , j)
    def numDistinct(self, s: str, t: str) -> int:
        return self.solve(s , t , len(s)-1 , len(t)-1)

""" shift one """
class Solution:
    def solve(self , s , t, i , j):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if s[i-1] == t[j-1]:
            take = self.solve(s , t, i-1 , j-1)
            move =   self.solve(s , t , i-1 , j)
            return (take + move)
        else:
            return self.solve(s , t, i-1 , j)
    def numDistinct(self, s: str, t: str) -> int:
        return self.solve(s , t , len(s) , len(t))

""" Top - down """

class Solution:
    def solve(self , s , t, i , j , memo):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if s[i-1] == t[j-1]:
            take = self.solve(s , t, i-1 , j-1 , memo)
            move =   self.solve(s , t , i-1 , j , memo)
            memo[i][j] =  (take + move)
            return memo[i][j]
        else:
            memo[i][j]  =  self.solve(s , t, i-1 , j , memo)
            return memo[i][j]
    def numDistinct(self, s: str, t: str) -> int:
        memo = [[-1 for j in range(len(t)+1)] for i in range(len(s)+1)]
        return self.solve(s , t , len(s) , len(t) , memo)

""" Bottom - up """
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
        for i in range(len(t)+1):
            dp[0][i] = 0
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1 , len(s)+1):
            for j in range(1 , len(t)+1):
                if s[i-1] == t[j-1]:
                    take = dp[i-1][j-1]
                    move = dp[i-1][j]
                    dp[i][j] = (take + move)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]
