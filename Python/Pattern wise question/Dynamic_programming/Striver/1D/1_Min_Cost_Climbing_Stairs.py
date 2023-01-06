"""
746. Min Cost Climbing Stairs
Easy
8.1K
1.3K
Companies
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
 Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


"""

 # Recursion
 class Solution:
    def solve(self, cost , n):
        if (n<0):
            return 0
        return min(self.solve(cost , n-2), self.solve(cost , n-1)) + cost[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = self.solve( cost , len(cost)-2)
        f2 = self.solve( cost , len(cost)-1)
        return min(f1 , f2)

# memorization
class Solution:
    def solve(self, cost , n , memo):
        if (n<0):
            return 0
        if (memo[n] != -1):
            return memo[n]
        memo[n] = cost[n] + min(self.solve(cost, n - 1, memo), self.solve(cost, n - 2, memo))

        return memo[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1 for _ in range(len(cost)+1)]
        # memo = [-1]*len(cost)
        f1 = self.solve( cost , len(cost)-2 , memo)
        f2 = self.solve( cost , len(cost)-1 , memo)
        return min(f1 , f2)










class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Loop through every cost after the first two steps
        for i in range(2, len(cost)):
            # Update the cheapest cost to step here
            cost[i] += min(cost[i-2], cost[i-1])

        # Cheapest cost of the last two steps is the answer
        return min(cost[len(cost)-2], cost[len(cost)-1])
