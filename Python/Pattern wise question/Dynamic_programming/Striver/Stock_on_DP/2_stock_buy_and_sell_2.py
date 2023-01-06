"""

122. Best Time to Buy and Sell Stock II
Medium
9.6K
2.5K
Companies
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

 On each day,
 you may decide to buy and/or sell the stock.
 You can only hold at most one share of the stock at any time.
  However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104


"""
class Solution:
    def solve(self , i , buy , prices , n):
        if i >= n:
            return 0
        if buy == 0:
            no = 0 + self.solve(i+1 , 0 , prices , n)
            take  = -prices[i] + self.solve(i+1 , 1 , prices , n)
            profit = max( take  , no)

        if buy == 1:
            profit = max(0 + self.solve(i+1 , 1 , prices , n) , prices[i] + self.solve(i+1 , 0 , prices , n))
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        return self.solve(0 , 0 , prices , n)

""" memorization """
class Solution:
    def solve(self , i , buy , prices , n , memo):
        if i >= n:
            return 0
        if memo[i][buy] != -1:
            return memo[i][buy]
        if buy == 0:
            no = 0 + self.solve(i+1 , 0 , prices , n , memo)
            take  = -prices[i] + self.solve(i+1 , 1 , prices , n , memo)
            profit = max( take  , no)
            memo[i][buy] = profit


        if buy == 1:
            profit = max(0 + self.solve(i+1 , 1 , prices , n , memo) , prices[i] + self.solve(i+1 , 0 , prices , n , memo))
            memo[i][buy] = profit
        memo[i][buy] = profit
        return memo[i][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[-1 for j in range(2)] for i  in range(n)]
        return self.solve(0 , 0 , prices , n , memo)

""" Bottom up """
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for j in range(2)] for i  in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        for  i in range(n-1 , -1 , -1):
            for j in range(2):
                if j == 0:
                    no = 0 + dp[i+1][0]
                    take = -prices[i] + dp[i+1][1]
                    profit = max(no , take)
                    dp[i][j] = profit
                if j == 1:
                    no = 0 + dp[i+1][1]
                    take = prices[i] + dp[i+1][0]
                    profit = max(no  , take)
                    dp[i][j] = profit
        return dp[0][0]


""" my fav solution """
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cost = prices[0]
        for i in range(1 , len(prices)):
            if prices[i] > cost:
                profit += prices[i] - cost
            cost = prices[i]
        return profit
