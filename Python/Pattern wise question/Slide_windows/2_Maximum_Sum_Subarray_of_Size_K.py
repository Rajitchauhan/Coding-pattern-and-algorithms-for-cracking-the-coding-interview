"""
Maximum Sum Subarray of Size K

Given an array of positive numbers and a positive number ‘k’,
find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
"""

class Sliding:
    def maxSum(self ,k ,  arr):
        start , end = 0 , 0
        sum = 0
        maxi = float('-inf')
        for end in range(len(arr)):
            sum += arr[end]
            if(end >= k-1):
                maxi = max(maxi , sum)
                sum -= arr[start]
                start += 1
        return maxi




if __name__ == "__main__":
    obj = Sliding()
    res = obj.maxSum(3 , [2 , 1 , 5 , 1 , 3, 2])
    print(f"max sum is {res}")
