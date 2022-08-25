"""
Given an array of integers, find the length of the longest sub-array with a sum that equals 0.

Examples:

Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
Output: 5
Explanation: The longest sub-array with
elements summing up-to 0 is {-2, 2, -8, 1, 7}

Input: arr[] = {1, 2, 3}
Output: 0
Explanation:There is no subarray with 0 sum

Input:  arr[] = {1, 0, 3}
Output:  1
Explanation: The longest sub-array with
elements summing up-to 0 is {0}

"""

def  maxsum(arr):
    #create hash map
    hashmap = {}
    maxlen = 0
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]

        if arr[i] is 0 and maxlen == 0:
            maxlen = 1
        if curr_sum is 0:
            maxlen = i+1

        if curr_sum in hashmap:
            maxlen = max(maxlen , i-hashmap[curr_sum])
        else:
            hashmap[curr_sum] = i

    return maxlen

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(maxsum(arr))
