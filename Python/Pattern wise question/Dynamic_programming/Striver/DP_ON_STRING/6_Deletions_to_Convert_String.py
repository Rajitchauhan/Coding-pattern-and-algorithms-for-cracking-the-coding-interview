"""

Problem Statement
Suggest Edit
You are given 2 non-empty strings “str” and “ptr” consisting of lowercase English alphabets only.
 Your task is to convert string “str” into string “ptr”.
  In one operation you can do either of the following on “str”:
Remove a character from any position in “str”.
Add a character to any position in “str”.
You have to find the minimum number of operations required to convert string “str” into “ptr”.
For Example:
If str = “abcd”, ptr = “anc”
In one operation remove str[3], after this operation str becomes “abc”.
In the second operation remove str[1], after this operation str becomes “ac”.
In the third operation add ‘n’ in str[1], after this operation str becomes “anc”.

Hence, the output will be 3.

Input Format :
The first line of the input contains an integer, 'T’, denoting the number of test cases.

The first line of each test case will contain two space-separated non-empty strings “str” and “ptr”.

Output Format :
For each test case, print the minimum number of operations required to convert string “str” into “ptr”.

Print a separate line for each test case.

Note :
You do not need to print anything, it has already been taken care of. Just implement the given function.

Constraints:
1 <= T <= 10
1 <= str.length, ptr.length <= 100

Time limit: 1 sec

Sample Input 1 :
2
abcd anc
aa aaa

Sample Output 1 :
3
1

Explanation For Sample Output 1:
For the first test case,
str = “abcd”, ptr = “anc”

In one operation remove str[3], after this operation str becomes “abc”.
In the second operation remove str[1], after this operation str becomes “ac”.
In the third operation add ‘n’ in str[1], after this operation str becomes “anc”.

Hence, the output will be 3.

For the second test case,
str = “aaa”, ptr = “aa”

In one operation remove str[2], after this operation str becomes “aa”.

Hence, the output will be 1.

Sample Input 2 :
2
cue dgo
edl xcqja

Sample Output 2 :
6
8


"""

"""  Recusion """
from os import *
from sys import *
from collections import *
from math import *

def solve(s , p , i , j):
    if i == 0 or j == 0:
        return 0
    if s[i-1] == p[j-1]:
        return 1 + solve(s ,p , i-1 , j-1)
    else:
        return max(solve(s , p , i-1 , j) , solve(s , p , i , j-1))

def canYouMake(s: str, p: str) -> int:
    # Write your code here.
    m = len(s)
    n = len(p)
    lcs = solve(s , p , m, n)
    ins = m - lcs
    deli = n - lcs
    return ins + deli



""" memorization """

def solve(s , p , i , j , memo):
    if i == 0 or j == 0:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    if s[i-1] == p[j-1]:
        memo[i][j] =  1 + solve(s ,p , i-1 , j-1 , memo)
        return memo[i][j]
    else:
        memo[i][j] =  max(solve(s , p , i-1 , j , memo) , solve(s , p , i , j-1 , memo))
        return memo[i][j]

def canYouMake(s: str, p: str) -> int:
    m = len(s)
    n = len(p)
    memo = [[-1 for i in range(n+1)] for j in range(m+1)]
    lcs = solve(s , p , m, n , memo)
    ins = m - lcs
    deli = n - lcs
    return ins + deli

""" Bottom up """


def canYouMake(s: str, p: str) -> int:
    # Write your code here.
    m = len(s)
    n = len(p)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1 , m+1):
        for j in range(1 , n+1):
            if s[i-1] == p[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    lcs = dp[m][n]
    ins = m - lcs
    deli = n - lcs
    return ins + deli
