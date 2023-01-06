"""

516. Longest Palindromic Subsequence
Medium
6.5K
262
Companies
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting
 some or no elements without changing the order of the remaining elements.



Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".


Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.

"""

""" Recursion """
class Solution:
    def solve(self , s1 , s2 , i , j):
        if i == 0 or j ==0:
            return 0
        if s1[i-1] == s2[j-1]:
            return 1 + self.solve(s1 , s2 , i-1 , j-1)
        else:
            return 0 + max(self.solve(s1 , s2 , i-1 , j) , self.solve(s1 , s2 , i , j-1))

    def longestPalindromeSubseq(self, s: str) -> int:
        lcs =  self.solve(s , s[::-1] , len(s) , len(s))
        return lcs

""" memorization """
class Solution:
    def solve(self , s1 , s2 , i , j , memo):
        if i == 0 or j ==0:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if s1[i-1] == s2[j-1]:
            memo[i][j] =  1 + self.solve(s1 , s2 , i-1 , j-1 , memo)
            return memo[i][j]
        else:
            memo[i][j] =  0 + max(self.solve(s1 , s2 , i-1 , j , memo) , self.solve(s1 , s2 , i , j-1 , memo))
            return memo[i][j]

    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[-1 for i in range(len(s)+1)] for j in range(len(s)+1)]
        return self.solve(s , s[::-1] , len(s) , len(s) , memo)

""" Bottom - up """
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        st = s[::-1]
        for i in range(1 , len(s)+1):
            for j in range(1 , len(s)+1):
                if s[i-1] == st[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

        return dp[len(s)][len(s)]
