"""


You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously
 (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6),
 profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000

"""

class Solution:
    def solve(self , i , trans , n , prices , memo):
        if i == n:
            return 0
        if trans == 0:
            return 0
        if memo[i][trans] != -1:
            return memo[i][trans]
        if trans%2==0:
            no = self.solve(i+1 , trans , n , prices , memo)
            take = -prices[i] + self.solve(i+1 , trans-1 , n , prices , memo)
            profit = max(take , no)
            memo[i][trans] = profit
        else:
            no = self.solve(i+1 , trans , n , prices , memo)
            take = prices[i]  + self.solve(i+1 , trans-1 , n, prices , memo)
            profit = max(take , no)
            memo[i][trans] = profit
        memo[i][trans] = profit
        return memo[i][trans]
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        memo = [[-1 for j in range(2*k+1)] for i in range(n)]
        return self.solve(0 ,k*2 , n , prices , memo)
