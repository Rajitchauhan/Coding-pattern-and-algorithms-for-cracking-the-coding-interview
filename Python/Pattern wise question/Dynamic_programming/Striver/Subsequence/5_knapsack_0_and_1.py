"""
You are given weights and values of N items,
put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
 Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1]
 and wt[0..N-1] which represent values and weights associated with N items respectively.
  Also given an integer W which represents knapsack capacity,
  find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
   You cannot break an item, either pick the complete item or dont pick it (0-1 property).
Example 1:
Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3

Example 2:
Input:
N = 3
W = 3
values[] = {1,2,3}
weight[] = {4,5,6}
Output: 0
Your Task:
Complete the function knapSack() which takes maximum capacity W,
 weight array wt[], value array val[],
 and the number of items n as a parameter and returns the maximum possible value you can get.
Expected Time Complexity: O(N*W).
Expected Auxiliary Space: O(N*W)
Constraints:
1 ≤ N ≤ 1000
1 ≤ W ≤ 1000
1 ≤ wt[i] ≤ 1000
1 ≤ v[i] ≤ 1000

"""
""" Recursion """
class Solution:
    def solve(self , W , wt , val , i):
        if i == 0:
            if wt[i] <=W:
                return val[0]
            else:
                return 0

        notTake = self.solve(W , wt , val , i-1)
        take = float("-inf")
        if wt[i] <=W:
            take = self.solve(W-wt[i] , wt , val , i-1) + val[i]
        return max(take , notTake)

    def knapSack(self,W, wt, val, n):
        return self.solve(W ,  wt , val , n-1)
""" Top - Down """
class Solution:
    def solve(self , W , wt , val , i , memo):
        if i == 0:
            if wt[i] <=W:
                return val[0]
            else:
                return 0
        if memo[i][W] != -1:
            return memo[i][W]

        notTake = self.solve(W , wt , val , i-1 ,memo)
        take = float("-inf")
        if wt[i] <=W:
            take = self.solve(W-wt[i] , wt , val , i-1 , memo) + val[i]
        memo[i][W] =  max(take , notTake)
        return memo[i][W]

    def knapSack(self,W, wt, val, n):
        memo = [[-1 for i in range(W+1)] for j in range(n)]

        return self.solve(W ,  wt , val , n-1 , memo)
