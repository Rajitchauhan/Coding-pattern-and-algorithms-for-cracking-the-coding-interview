"""
Problem Description

Given a string A,
 find the common palindromic sequence ( A sequence which does not need to be contiguous and is a pallindrome),
  which is common in itself.

You need to return the length of longest palindromic subsequence in A.
NOTE:
Your code will be run on multiple test cases (<=10). Try to come up with an optimised solution.

Problem Constraints
 1 <= |A| <= 1005

Input Format
First and only argument is an string A.

Output Format
Return a integer denoting the length of longest palindromic subsequence in A.

Example Input
Input 1:

 A = "bebeeed"

Example Output
Output :
 4
"""
def longest_palindrome_subsequence(A):
    B = A[::-1]
    m , n = len(A) , len(B)

    t = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif A[i-1]==B[j-1]:
                t[i][j] = 1+ t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1] , t[i-1][j])

    return t[m][n]

A = "bebeeed"
print(longest_palindrome_subsequence(A))
