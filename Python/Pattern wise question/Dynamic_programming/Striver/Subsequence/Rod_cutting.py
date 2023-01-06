"""

Rod Cutting
MediumAccuracy: 60.66%Submissions: 54K+Points: 4
Given a rod of length N inches and an array of prices,
price[]. pricei denotes the value of a piece of length i.
 Determine the maximum value obtainable by cutting up the rod and selling the pieces.



Example 1:

Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by
cutting in two pieces of lengths 2 and
6, i.e., 5+17=22.
Example 2:

Input:
N=8
Price[] = {3, 5, 8, 9, 10, 17, 17, 20}
Output: 24
Explanation:
The maximum obtainable value is
24 by cutting the rod into 8 pieces
of length 1, i.e, 8*3=24.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function cutRod()
which takes the array A[] and its size N as inputs and returns the maximum price obtainable.


Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 1000
1 ≤ Ai ≤ 105

"""

# Recursion
class Solution:
    def solve(self , i , price , n):
        if i == 0:
            return price[0]*n
        no_take = self.solve(i-1 , price , n) + 0
        take = -1
        rodLen = i + 1
        if (rodLen <= n):
            take = price[i] + self.solve(i-1 , price , n - rodLen)

        return max(no_take , take)

    def cutRod(self, price, n):
        #code here
        return self.solve(n-1 , price , n)

# memorization
class Solution:
    def solve(self , i , price , n , memo):
        if i == 0:
            return price[0]*n
        if memo[i][n] != -1:
            return memo[i][n]
        no_take = self.solve(i-1 , price , n , memo) + 0
        take = -10000000
        rodLen = i + 1
        if (rodLen <= n):
            take = price[i] + self.solve(i , price , n - rodLen , memo)

        memo[i][n] =  max(no_take , take)
        return memo[i][n]

    def cutRod(self, price, n):
        #code here
        memo = [[-1 for i in range(n+1)] for j in range(n)]
        return self.solve(n-1 , price , n , memo)


# Bottom up

class Solution:

    def cutRod(self, price, n):
        #code here
        dp = [[0 for i in range(n+1)] for j in range(n)]
        for i in range(n+1):
            dp[0][i] = price[0]*i

        for i in range(1 , n):
            for j in range(n+1):
                no_take = dp[i-1][j] + 0
                take = -1
                rodlen = i + 1
                if rodlen <= j:
                    take = dp[i][j-rodlen] + price[i]
                dp[i][j] = max(take , no_take)

        return dp[n-1][n]
