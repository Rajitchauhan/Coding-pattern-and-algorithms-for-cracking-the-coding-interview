"""
problem :: Given n non-negative integers representing an elevation map
            where the width of each bar is 1,
            compute how much water it is able to trap after raining.

Examples:

Input: arr[]   = {2, 0, 2}
Output: 2
Explanation:
The structure is like below


We can trap 2 units of water in the middle gap.

Input: arr[]   = {3, 0, 2, 0, 4}
Output: 7
Explanation:
Structure is like below


We can trap "3 units" of water between 3 and 2,
"1 unit" on top of bar 2 and "3 units" between 2
and 4.  See below diagram also.

Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6


"""

def rain_water_trap(arr , n):
    max_left=[0]*n
    max_right=[0]*n
    max_left[0]=arr[0]

    for i in range(1 , n):
        max_left[i] = max(max_left[i-1] , arr[i])

    max_right[n-1] = arr[n-1]
    for i in range(n-2 , -1 , -1):
        max_right[i] = max(max_right[i+1] , arr[i])

    water = [0]*n
    for i in range(n):
        water[i] = (min(max_left[i] , max_right[i]) - arr[i])

    #print(water)
    sum = 0
    for i in range(n):
        sum = sum + water[i]

    return sum

arr= [3, 0, 2, 0, 4]
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
print(rain_water_trap(arr , n))


"""


# Python program to find
# maximum amount of water that can
# be trapped within given set of bars.
# Space Complexity : O(1)

def findWater(arr, n):

    # initialize output
    result = 0

    # maximum element on left and right
    left_max = 0
    right_max = 0

    # indices to traverse the array
    lo = 0
    hi = n-1

    while(lo <= hi):

        if(arr[lo] < arr[hi]):

            if(arr[lo] > left_max):

                # update max in left
                left_max = arr[lo]
            else:

                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo+= 1

        else:

            if(arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi-= 1

    return result

# Driver program

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)

print("Maximum water that can be accumulated is ",
        findWater(arr, n))

# This code is contributed
# by Anant Agarwal.
Output:

Maximum water that can be accumulated is 6
Complexity Analysis:
Time Complexity: O(n).
Only one traversal of the array is needed.
Auxiliary Space: O(1).
As no extra space is required.
"""
