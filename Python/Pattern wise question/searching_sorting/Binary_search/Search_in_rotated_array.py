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


arr=[11 , 12 , 15 , 18 , 2 ,5 , 6 , 8]
#arr=[15,18,2,3,6,12]
#arr=[8,9,10,2,5,6]
n=len(arr)
x=12
res = search_in_rotated_array(arr,x ,  n)
if(res != -1):
    print(f'Element at index {res} ')
else:
    print("element is not present")
