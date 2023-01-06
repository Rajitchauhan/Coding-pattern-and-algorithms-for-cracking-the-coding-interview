"""

300. Longest Increasing Subsequence
Medium
15.9K
292
Companies
Given an integer array nums, return the length of the longest strictly increasing
subsequence
.


Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

"""

class Solution:
    def solve(self , i , nums ,pre):
        if i == len(nums):
            return 0
        no = 0 + self.solve(i+1 , nums ,pre)
        take = -1
        if pre == -1 or nums[i] > nums[pre]:
            take = 1 + self.solve(i+1 , nums ,i)
        return max(take , no)
    def lengthOfLIS(self, nums: List[int]) -> int:
        pre = -1
        n = len(nums)
        return self.solve(0 , nums,  pre)


# Gives Tle memorization
class Solution:
    def solve(self , i , nums ,pre , memo):
        if i == len(nums):
            return 0
        if memo[i][pre] != -1:
            return memo[i][pre]
        no = self.solve(i+1 , nums ,pre , memo)
        take = -1
        if pre == -1 or(nums[i] > nums[pre]):
            take = 1 + self.solve(i+1 , nums ,i , memo)

        memo[i][pre] = max(take , no)
        return memo[i][pre]
    def lengthOfLIS(self, nums: List[int]) -> int:
        pre = -1
        n = len(nums)
        memo = [[-1 for j in range(n+1)] for i  in range(n)]
        return self.solve(0 , nums,  pre , memo)



# nums = [10,9,2,5,3,7,101,18]
# dp[0] = [10]
# Iterations
# dp = [9] length = 1
# dp = [2]  length = 1
# dp = [2,5]  length = 2
# dp = [2,3] length = 2
# dp = [2,3,7] length = 3
# dp = [2,3,7,101] length = 4
# dp = [2,3,7,18] length = 4
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

		#Handling base case
        if nums == None or len(nums) == 0:
            return 0

		#Initialize a dp array with the same size as nums
		# dp = [0,0,0,0,0,0,0,0]
        dp = [0]*len(nums)
		# The first element of dp array will be nums[0] since it is the only element as of now
        dp[0] = nums[0]

		# Increment the length to 1 which is the size of our dp array
        length = 1

		# Iterate over the remaining elements

        for i in range(1,len(nums)):
		# If the previous element in dp array is less than nums[i] we append nums[i] to dp array and increment length by 1
            if dp[length-1] < nums[i]:
                dp[length] = nums[i]
                length +=1
            else:
			# Otherwise we will do a binary search over the previous elements in the dp array to find the element that is just greater than nums[i] ( Ceiling )
                index = self.binarySearch(dp[:length],nums[i])
				# We replace element at the found index by nums[i]
                dp[index] = nums[i]

        return length


    def binarySearch(self,arr,target):

        low = 0
        high = len(arr)-1
        res = -1
        while low < high:
            mid = low+(high-low)//2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid+1
            else:
                high = mid
        return low



# print LIS

from os import *
from sys import *
from collections import *
from math import *

from typing import List


def divisibleSet(arr: List[int]) -> List[int]:
    # Write your code here.
    arr.sort()
    n = len(arr)

    dp = [1]*n
    hash = [0]*n
    maxi = -1
    for i in range(n):
        hash[i] = i
        for j in range(i):
            if arr[i] % arr[j] == 0:
                #dp[i] = max(dp[i] , 1+dp[j])
                if dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
                    hash[i] = j
        #maxi = max(maxi , dp[i])
        if dp[i] > maxi:
            maxi = dp[i]
            last_index = i
    res = []
    res.append(arr[last_index])
    while hash[last_index] != last_index:
        last_index = hash[last_index]
        res.append(arr[last_index])
    return res[::-1]

    return maxi
