"""


Given two strings word1 and word2,
 return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

"""

"""  Recursion """
class Solution:
    def solve(self , str1 , str2 , i , j):
        if i < 0:
            return j+1
        if j < 0:
            return i+1
        if str1[i] != str2[j]:
            return 1 + min(self.solve(str1  , str2 , i-1 , j)
             ,  min(self.solve(str1  , str2 , i-1 , j-1)
              , self.solve(str1  , str2 , i , j-1)))
        else:
            return 0 +  self.solve(str1  , str2 , i-1 , j-1)

    def minDistance(self, word1: str, word2: str) -> int:
        i , j = len(word1) , len(word2)
        return self.solve(word1 , word2 , i-1 , j-1)

""" recursion one shift """
class Solution:
    def solve(self , str1 , str2 , i , j):
        if i == 0:
            return j
        if j == 0:
            return i
        if str1[i-1] != str2[j-1]:
            return 1 + min(self.solve(str1  , str2 , i-1 , j)
             ,  min(self.solve(str1  , str2 , i-1 , j-1)
              , self.solve(str1  , str2 , i , j-1)))
        else:
            return 0 +  self.solve(str1  , str2 , i-1 , j-1)

    def minDistance(self, word1: str, word2: str) -> int:
        i , j = len(word1) , len(word2)
        return self.solve(word1 , word2 , i , j)


""" memorization """
class Solution:
    def solve(self , str1 , str2 , i , j , memo):
        if i == 0:
            return j
        if j == 0:
            return i
        if memo[i][j] != -1:
            return memo[i][j]
        if str1[i-1] != str2[j-1]:
            memo[i][j] =  1 + min(self.solve(str1  , str2 , i-1 , j , memo)
             ,  min(self.solve(str1  , str2 , i-1 , j-1 , memo)
              , self.solve(str1  , str2 , i , j-1 , memo)))
            return memo[i][j]
        else:
            memo[i][j]  = 0 +  self.solve(str1  , str2 , i-1 , j-1 , memo)
            return memo[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        i , j = len(word1) , len(word2)
        memo = [[-1 for _ in range(j+1)] for _ in range(i+1)]
        return self.solve(word1 , word2 , i , j , memo)


""" Bottom - up """
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        i , j = len(word1) , len(word2)
        dp = [[0 for _ in range(j+1)] for _ in range(i+1)]
        for m in range(j+1):
            dp[0][m] = m
        for n in range(i+1):
            dp[n][0] = n
        for m in range(1 , i+1):
            for n in range(1 , j+1):
                if word1[m-1] == word2[n-1]:
                    dp[m][n] = 0 + dp[m-1][n-1]
                else:
                    dp[m][n] = 1 + min(dp[m-1][n] ,
                     min(dp[m-1][n-1] , dp[m][n-1]))

        return dp[i][j]
