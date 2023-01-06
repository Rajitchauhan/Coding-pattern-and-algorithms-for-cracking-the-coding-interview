"""

Given a non-empty array nums containing only positive integers,
 find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

"""
"""  Recursion """
class Solution:
    def  solve(self , i , nums , tar):
        if tar == 0:
            return True
        if i == 0:
            return nums[0] == tar

        no = self.solve(i-1 , nums , tar)
        take = False
        if nums[i] <= tar:
            take = self.solve(i-1 , nums , tar-nums[i])
        return (no or take)

    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for i in nums:
            sum += i
        n = len(nums)
        if sum%2 != 0:
            return False
        else:
            return self.solve(n-1 , nums , sum // 2)

""" Top- deon """


""" Bottom - up """
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for i in nums:
            sum += i
        n = len(nums)
        tar = sum // 2
        dp = [[False for i in range(tar + 1)] for j in range(n)]

        if sum % 2 != 0:
            return False
        else:
            for i in range(n):
                dp[i][0] = True
            if  nums[0] <= tar:
                dp[0][nums[0]] = True
            for i in range(1 , n):
                for j in range(1 , tar+1):
                    no = dp[i-1][j]
                    take = False
                    if nums[i]<=j:
                        take = dp[i-1][j-nums[i]]
                    dp[i][j] = take or no
            return dp[n-1][tar]
