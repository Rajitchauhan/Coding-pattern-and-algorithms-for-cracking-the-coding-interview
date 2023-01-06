"""

Given two strings text1 and text2, return the length of their longest common subsequence.
 If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters
 (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.



"""

""" Recursion """

def solve(i , j , s , t):
    if i < 0 or j < 0:
        return 0
    if s[i] == t[j]:
        return 1 + solve(i-1 , j-1 , s , t)
    else:
        return  max(0 + solve(i-1 , j , s , t) , 0 + solve(i , j-1 , s , t))


def lcs(s, t) :
    i = len(s)
    j = len(t)
    return solve(i-1 , j-1 , s, t)

""" Recursion 2 (one + len) """

from sys import stdin
def solve(i , j , s , t , memo):
    if i == 0 or j == 0:
        return 0
    if s[i-1] == t[j-1]:
        return 1 + solve(i-1 , j-1 , s , t , memo)
    else:
        return  max(solve(i-1 , j , s , t  , memo) , solve(i , j-1 , s , t , memo))

def lcs(s, t):
    i = len(s)
    j = len(t)
    return solve(i , j , s, t , memo)
#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))

""" memorization """
from sys import stdin
def solve(i , j , s , t , memo):
    if i == 0 or j == 0:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    if s[i-1] == t[j-1]:
        memo[i][j] =   1 + solve(i-1 , j-1 , s , t , memo)
        return memo[i][j]
    else:
        memo[i][j] =   max(solve(i-1 , j , s , t  , memo) , solve(i , j-1 , s , t , memo))
        return memo[i][j]

def lcs(s, t):
    i = len(s)
    j = len(t)
    memo = [[-1 for b in range(j+1)] for a in range(i+1)]
    return solve(i , j , s, t , memo)


""" Bottom - up """


def lcs(s, t):
    m = len(s)
    n = len(t)
    dp = [[0 for b in range(n+1)] for a in range(m+1)]
    for i in range(1 , m+1):
        for j in range(1 , n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    return dp[m][n]
