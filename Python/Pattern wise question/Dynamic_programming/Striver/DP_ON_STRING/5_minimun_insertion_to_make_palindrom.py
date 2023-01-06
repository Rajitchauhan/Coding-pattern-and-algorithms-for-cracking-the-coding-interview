"""
1312. Minimum Insertion Steps to Make a String Palindrome
Hard
2.7K
33
Companies
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.



Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.


"""
""" memorization """
class Solution:
    def solve(self , s , t , i , j , dp):
        if i ==0 or j ==0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s[i-1] == t[j-1]:
            dp[i][j] = 1 + self.solve(s , t , i-1 , j-1 , dp)
            return dp[i][j]
        else:
            dp[i][j] = max(self.solve(s , t , i-1 , j , dp) , self.solve(s , t , i, j-1 , dp))
            return dp[i][j]
    def minInsertions(self, s: str) -> int:
        m = len(s)
        n = m
        dp = [[-1 for  j in range(n+1)] for i in range(m+1)]
        st = s[::-1]
        lps = self.solve(s , st , m, n , dp)
        return (m - lps)
       

""" Bottom  - up """
class Solution:
    def minInsertions(self, s: str) -> int:
        m = len(s)
        n = m
        dp = [[0 for  j in range(n+1)] for i in range(m+1)]
        st = s[::-1]
        for i in range(1 , m+1):
            for j in range(1 , n+1):
                if s[i-1] == st[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        return (m - dp[m][n])
