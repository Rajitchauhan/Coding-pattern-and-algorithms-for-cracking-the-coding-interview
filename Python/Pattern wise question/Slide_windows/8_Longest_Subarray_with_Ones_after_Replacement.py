"""
https://leetcode.com/problems/max-consecutive-ones-iii

1004. Max Consecutive Ones III
Medium

5146

65

Add to List

Share
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length

TC: O(N)
SC: O(1)
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start  = 0
        mini = 0
        maxFreq = 0
        for end in range(len(nums)):
            if(nums[end] == 1):
                maxFreq += 1
            if((end - start + 1) - maxFreq ) > k:
                if(nums[start] == 1):
                    maxFreq -= 1

                start += 1
            mini = max(mini , end - start + 1)
        return mini
