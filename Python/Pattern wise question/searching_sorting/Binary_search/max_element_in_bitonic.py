"""
problem :: find maximum element in Bitonic Array
Ex :: 1 , 3 , 8 , 12 , 4 , 2
output :: 12
"""
def peak(arr ,  n):
    low , high = 0 , n-1
    while(low<=high):
        mid = low+(high-low)//2
        if mid==0:
            if arr[mid]>arr[mid+1]:
                return arr[mid]
            else:
                return arr[mid+1]
        elif mid == n-1:
            if arr[mid]>arr[mid-1]:
                return arr[mid]
            else:
                return arr[mid-1]
        else:
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return arr[mid]
            elif arr[mid]>arr[mid-1]:
                low = mid + 1
            else:
                high = mid-1

arr=[1 , 3 , 8 , 12 , 4 , 2]
n=len(arr)
print(peak(arr , n))
