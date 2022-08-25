"""
problem  :: Peak element
Ex ::  5 , 10 , 20 , 15
output :: 20
"""

def peak(arr , x , n):
    low , high = 0 , n-1
    while(low<=high):
        mid = low+(high-low)//2
        if (mid>0 and mid < n-1):
            if arr[mid]>arr[mid-1] and arr[mid]> arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid-1]:
                low = mid+1
            else:
                high = mid-1
        elif mid == 0:
            if arr[mid]> arr[mid+1]:
                return mid
            else:
                return mid+1
        elif mid == n-1:
            if arr[mid]>=arr[n-2]:
                return n-1
            else:
                return n-2

arr=[5 , 10 , 20 , 15]
arr=[5 , 10 , 15 , 20]
arr=[5 , 20 , 10 , 15]
arr=[20 , 10 , 5 , 15]

x=20
n=len(arr)
print(peak(arr , x , n))
