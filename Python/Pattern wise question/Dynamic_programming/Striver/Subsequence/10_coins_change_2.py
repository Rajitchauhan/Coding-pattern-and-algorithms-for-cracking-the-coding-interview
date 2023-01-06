"""
518. Coin Change II
Medium
6.6K
120
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.



Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""
# Recursion
class Solution:
    def solve(self , i , amount , coins):
        if i == 0:
            if amount % coins[0] == 0:
                return 1
            return 0
        if amount == 0:
            return 1

        no_take = self.solve(i-1 , amount , coins)
        take = 0
        if coins[i] <= amount:
            take = self.solve(i , amount - coins[i] , coins)
        return (take + no_take)
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        return self.solve(n-1 , amount , coins)

# memorization

class Solution:
    def solve(self , i , amount , coins , memo):
        if i == 0:
            if amount % coins[0] == 0:
                return 1

            return 0
        if memo[i][amount] != -1:
            return memo[i][amount]
        if amount == 0:
            return 1

        no_take = self.solve(i-1 , amount , coins , memo)
        take = 0
        if coins[i] <= amount:
            take = self.solve(i , amount - coins[i] , coins , memo)
        memo[i][amount] = (take + no_take)
        return memo[i][amount]
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[-1 for j in range(amount+1)] for i in range(n)]
        return self.solve(n-1 , amount , coins , memo)


#  Bottom up
class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for j in range(amount+1)] for i in range(n)]
        for i in range(amount+1):
            if i%coins[0] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
        for j in range(n):
            dp[j][0] = 1

        for  i in range(1 , n):
            for j in range(1 , amount+1):
                no_take = dp[i-1][j]
                take = 0
                if coins[i] <= j:
                    take = dp[i][j- coins[i]]
                dp[i][j] = take + no_take
        return dp[n-1][amount]
