"""


You are given two strings s and t.
 Now your task is to print all longest common sub-sequences in lexicographical order.

Example 1:

Input: s = abaaa, t = baabaca
Output: aaaa abaa baaa
Example 2:

Input: s = aaa, t = a
Output: a
Your Task:
You do not need to read or print anything.
 Your task is to complete the function all_longest_common_subsequences()
  which takes string a and b as first and second parameter respectively
  and returns a list of strings
  which contains all possible longest common subsequences in lexicographical order.


Expected Time Complexity: O(n4)
Expected Space Complexity: O(K * n) where K is a constant less than n.


Constraints:
1 ≤ Length of both strings ≤ 50

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestCommonSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def longestCommonSubsequence(a, b):
        m = len(a)
        n = len(b)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1 , m+1):
            for j  in range(1 , n+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        i , j = m , n
        res = []
        while(i > 0 and j > 0):
            if a[i-1] == b[j-1]:
                res.append(a[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1

        return res[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
