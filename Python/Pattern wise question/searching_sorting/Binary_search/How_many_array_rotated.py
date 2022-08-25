"""
problem : how many times sorted array is rotated
Ex ::Sorted Array : 2 , 5 , 6, 8 , 11 , 12 , 15 , 18
Given array    :    11 , 12 , 15 , 18 , 2 ,5 , 6 , 8

ouput : 4
"""
def rotation_time(arr  , n):
    low = 0
    high = n-1
    while(low<=high):
        if arr[low]<=arr[high]:
            return low
        mid = low+(high-low)//2
        pre = (mid-1+n)%n
        next = (mid+1)%n
        if arr[mid]<arr[pre] and arr[mid]<=arr[next]:
            return mid
        elif arr[mid]>=arr[low]:
            low = mid+1
        elif(arr[mid]<arr[high]):
            high = mid-1
        else:
            return 0
    return  -1
arr=[11 , 12 , 15 , 18 , 2 ,5 , 6 , 8]
#arr=[15,18,2,3,6,12]
#arr=[8,9,10,2,5,6]
n=len(arr)
res = rotation_time(arr ,  n)
if(res != -1):
    print(f'Array is rotated {res} times')
else:
    print("Can not be determine")
