"""


You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously
 (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later,
 as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105

"""

""" Recursion """
class Solution:
    def solve(self , i , buy , cap , prices , n):
        if i == n:
            return 0
        if cap == 0:
            return 0
        if buy == 0:
            no = self.solve(i+1 , 0 , cap , prices , n)
            take = -prices[i]  + self.solve(i+1 , 1 , cap , prices , n)
            profit = max(no , take)
        if buy == 1:
            no = self.solve(i+1 , 1 , cap , prices , n)
            take = self.solve(i+1 , 0 , cap-1 , prices , n) + prices[i]
            profit = max(no , take)
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        n  = len(prices)
        return self.solve(0 , 0 , 2 , prices,  n)



""" memorization (TLE) """
class Solution:
    def solve(self , i , buy , cap , prices , n , memo):
        if i == n:
            return 0
        if cap == 0:
            return 0
        if memo[i][buy][cap] != -1:
            return memo[i][buy][cap]
        if buy == 0:
            no = self.solve(i+1 , 0 , cap , prices , n ,memo)
            take = -prices[i]  + self.solve(i+1 , 1 , cap , prices , n , memo)
            profit = max(no , take)
            memo[i][buy][cap] = profit
        if buy == 1:
            no = self.solve(i+1 , 1 , cap , prices , n , memo)
            take = self.solve(i+1 , 0 , cap-1 , prices , n ,memo) + prices[i]
            profit = max(no , take)
            memo[i][buy][cap] = profit
        memo[i][buy][cap] = profit
        return memo[i][buy][cap]

    def maxProfit(self, prices: List[int]) -> int:
        n  = len(prices)
        memo =[[[-1 for k in range(3)]for  j  in  range(2)]for i in range(n)]
        return self.solve(0 , 0 , 2 , prices,  n , memo)

""" Bottom up """



""" Recursion  with even -  odd  """
class Solution:
    def solve(self , i ,trans , prices , n ):
        if i == n:
            return 0
        if trans == 0:
            return 0
        if trans%2 == 0:
            no = self.solve(i+1 , trans , prices , n)
            take = -prices[i]  + self.solve(i+1  , trans-1 , prices , n)
            profit = max(no , take)
        else:
            no = self.solve(i+1  , trans , prices , n)
            take = self.solve(i+1  , trans-1 , prices , n) + prices[i]
            profit = max(no , take)
        return  profit

    def maxProfit(self, prices: List[int]) -> int:
        n  = len(prices)
        return self.solve(0 , 4 , prices,  n )

""" memorization """
class Solution:
    def solve(self , i ,trans , prices , n  , memo):
        if i == n:
            return 0
        if trans == 0:
            return 0
        if memo[i][trans] != -1:
            return memo[i][trans]

        if trans%2 == 0:
            no = self.solve(i+1 , trans , prices , n , memo)
            take = -prices[i]  + self.solve(i+1  , trans-1 , prices , n , memo)
            profit = max(no , take)
            memo[i][trans] = profit
        else:
            no = self.solve(i+1  , trans , prices , n , memo)
            take = self.solve(i+1  , trans-1 , prices , n , memo) + prices[i]
            profit = max(no , take)
            memo[i][trans] = profit

        memo[i][trans] = profit
        return memo[i][trans]

    def maxProfit(self, prices: List[int]) -> int:
        n  = len(prices)
        memo = [[-1 for i in range(4+1)] for j in range(n)]
        return self.solve(0 , 4 , prices,  n  , memo)
