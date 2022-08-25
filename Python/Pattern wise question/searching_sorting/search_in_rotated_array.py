"""
Problem :: suppose you have an array sorted in ascending order is rotated
           at some pivot unknown to you beforehand .
           (i.e :: [0,1,2,4,5,6,7]  might become
            [4,5,6,7,0,1,2] )
         you are given a target value to search , if found in the array return its index
         otherwise -1
        # you may assume no duplicates exists in array
"""

def search_in_rotated_array(arr , target):
    left , right = 0 , len(arr) - 1
    mid = 0

    while(left <= right):
        mid = (left + right) // 2
        if (target == arr[mid]):
            return mid
        elif(arr[left] <= arr[mid]):
            if arr[left] <= target <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] <= target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return - 1

arr = [4,5,6,7,0,1,2]
target = 0

result = search_in_rotated_array(arr , target)

if result!= -1:
    print(f'target is found at index {str(result)}')
else:
    print(f'target is not found ')
