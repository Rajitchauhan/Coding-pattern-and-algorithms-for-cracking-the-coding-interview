"""

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-'
 before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-'
before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.



Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1


Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000


"""

""" Recursion """
class Solution:
    def solve(self , i ,nums ,  tar):
        if i==0:
            if tar == 0  and nums[0] == 0:
                return 2
            if tar == 0 or nums[0] == tar:
                return 1
            else:
                return 0
        no = self.solve(i-1 , nums , tar)
        take = 0
        if nums[i] <= tar:
            take = self.solve(i-1 , nums , tar-nums[i])
        return (take + no)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum = 0
        for i in nums:
            sum += i
        if (sum-target)%2 !=0:
            return False
        if (sum-target) < 0:
            return False
        tar = (sum-target)//2
        return self.solve(len(nums)-1 , nums , tar)

"""  Memoirazation """

class Solution:
    def solve(self , i ,nums ,  tar , memo):
        if i==0:
            if tar == 0  and nums[0] == 0:
                return 2
            if tar == 0 or nums[0] == tar:
                return 1
            else:
                return 0
        if memo[i][tar] != -1:
            return memo[i][tar]
        no = self.solve(i-1 , nums , tar , memo)
        take = 0
        if nums[i] <= tar:
            take = self.solve(i-1 , nums , tar-nums[i] , memo)
        memo[i][tar] =  (take + no)
        return memo[i][tar]
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum = 0
        for i in nums:
            sum += i
        if (sum-target)%2 !=0:
            return 0
        if (sum-target) < 0:
            return 0
        tar = (sum-target)//2
        memo = [[-1 for i in range(tar+1) ] for j in range(len(nums))]
        return self.solve(len(nums)-1 , nums , tar , memo)
""" Bottom-up """
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum = 0
        for i in nums:
            sum += i
        if (sum-target)%2 !=0:
            return 0
        if (sum-target) < 0:
            return 0
        tar = (sum-target)//2
        n = len(nums)
        dp = [[0 for i in range(tar+1) ] for j in range(n)]
        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if nums[0] != 0 and nums[0] <= tar:
            dp[0][nums[0]] = 1
        for i in range(1 , n):
            for j in range(tar+1):
                no = dp[i-1][j]
                take  = 0
                if nums[i] <= j:
                    take =  dp[i-1][j-nums[i]]
                dp[i][j] = (take + no)
        return dp[n-1][tar]

                
