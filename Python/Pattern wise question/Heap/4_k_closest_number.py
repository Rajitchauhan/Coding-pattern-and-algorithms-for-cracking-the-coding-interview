"""
Given a sorted array arr[] and a value X, find the k closest elements to X in arr[].

Examples:

Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42,
               45, 48, 50, 53, 55, 56}
Output: 30 39 42 45
"""

def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    res = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            res = nums[mid]
            high = mid - 1
        else:
            return mid + 1     # key found

    return res
def k_closed(nums , n , k , target):
    i= binarySearch(nums , target)
    left=i
    right = i+1

    while k>0:
        if left < 0 or right<n and abs(nums[left]-target) > abs(nums[right]-target):
            right += 1
        else:
            left -= 1

        k -= 1

    return nums[left+1 : right]

nums = [12, 16, 22, 30, 35, 39, 42,
        45, 48, 50, 53, 55, 56]
k=4
target = 35
n=len(nums)
print(k_closed(nums ,n , k , target))
# output : [30, 35, 39, 42]
