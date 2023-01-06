"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve.
 You may complete as many transactions as you like
  (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day
 (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously
 (i.e., you must sell the stock before you buy again).


Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000

"""

class Solution:
    def solve(self , i , buy , prices, n , memo):
        if i >= n:
            return 0
        if memo[i][buy] != -1:
            return memo[i][buy]
        if buy == 0:
            no = self.solve(i+1 , 0 , prices , n , memo)
            take =  -prices[i] +  self.solve(i+1 , 1 , prices , n , memo)
            profit = max(no , take)
            memo[i][buy] = profit
        if buy == 1:
            no = self.solve(i+1 , 1 , prices , n , memo)
            take = prices[i] + self.solve(i+2 , 0 , prices , n , memo)
            profit = max(no , take)
            memo[i][buy] = profit
        memo[i][buy] = profit
        return profit
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[-1 for j in range(2)] for i in range(n)]
        return self.solve(0 , 0 , prices , n , memo)


""" Bottom - up """

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for j in range(2)] for i in range(n+2)]
        dp[n][0] = dp[n][1]= dp[n+1][0] = dp[n+1][1] = 0
        for i in range(n-1 , -1  , -1):
            for j in range(2):
                if j ==0:
                    no = dp[i+1][0]
                    take = -prices[i] + dp[i+1][1]
                    profit = max(no , take)
                    dp[i][j] = profit
                if j == 1:
                    no = dp[i+1][1]
                    take = prices[i] + dp[i+2][0]
                    profit = max(no , take)
                    dp[i][j] = profit

        return dp[0][0]
