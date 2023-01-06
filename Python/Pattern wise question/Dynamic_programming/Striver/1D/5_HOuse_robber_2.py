"""
You are a professional robber planning to rob houses along a street.
 Each house has a certain amount of money stashed.
  All houses at this place are arranged in a circle.
   That means the first house is the neighbor of the last one.
    Meanwhile, adjacent houses have a security system connected,
     and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
 return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

"""
""" Recursion  """
class Solution:
    def  solve1(self,i , nums):
        if(i==0):
            return nums[i]
        if(i<0): return 0
        take = self.solve1(i-2 , nums) + nums[i]
        no =self.solve1(i-1  , nums) + 0
        return max(take , no)
    def  solve2(self , i , nums):
        if(i==1):
            return nums[i]
        if(i<=0): return 0
        take = self.solve2(i-2 , nums) + nums[i]
        no = self.solve2(i-1  , nums) + 0
        return max(take , no)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==1):
            return nums[n-1]
        f1 = self.solve1(n-2 , nums)
        f2 = self.solve2(n-1 , nums)
        return max(f1 , f2)

class Solution:
    def  solve1(self, nums): # exclude first 1 - ()n-1)
        n = len(nums)
        dp = [0]*n
        dp[0] = 0
        dp[1] = nums[1]
        dp[2] = max(nums[1] , nums[2])
        for i in range(2 , n):
            take = nums[i]
            if i > 2:
                take += dp[i-2]
            no = dp[i-1]
            dp[i] = max(take , no)
        return dp[n-1]
    def  solve2(self , nums): # 0 to n-2 exclude last element
        n = len(nums)-1
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1 , n):
            take = nums[i]
            if i >1:
                take += dp[i-2]
            no = dp[i-1]
            dp[i] = max(take , no)
        return dp[n-1]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==1):
            return nums[n-1]
        if(n==2):
            return max(nums[0] , nums[1])
        f2 = self.solve2(nums) # 0 to n-2 exclude last element

        f1 = self.solve1(nums)
        return max(f1 , f2)
