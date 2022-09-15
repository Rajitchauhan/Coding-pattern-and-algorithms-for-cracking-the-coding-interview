"""
Problem Statement #
Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous subarray
whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

"""
#Bruite Force Approach 
class Sliding_variable1:
    def small_subArr(self ,S ,  arr):
        maxi = float("inf")
        for i in range(len(arr)):
            sum = 0
            for j in range(i , len(arr)):
                sum += arr[j]
                if(sum >= S):
                    maxi = min(maxi , j - i + 1)
        return maxi

class Sliding_variable:
    def small_subArr(self ,S ,  arr):
        start , end = 0 , 0
        sum = 0
        maxi = float('inf')
        for end in range(len(arr)):
            sum += arr[end]
            while(sum >= S):
                maxi = min(maxi , (end - start + 1))
                sum -= arr[start]
                start += 1
        return maxi



if __name__ == "__main__":
    obj = Sliding_variable()
    res = obj.small_subArr(7 , [2, 1, 5, 2, 3, 2])
    #[2, 1, 5, 2, 8], S=7
    print(f"Broute force max sum is {res}")

"""
The time complexity of the above algorithm will be O(N).
The outer for loop runs for all elements and the inner while loop processes each element only once,
therefore the time complexity of the algorithm will be O(N+N)
which is asymptotically equivalent to O(N).

Space Complexity #
The algorithm runs in constant space O(1).
"""
