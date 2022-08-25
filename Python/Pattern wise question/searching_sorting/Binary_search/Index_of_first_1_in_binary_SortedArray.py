"""
problem :: index of first '1' in binary(00 , 11 , 01 , 10) sorted array
Ex :: 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,............infinite
output :: 18
"""
def index_first_in_infinite(arr , key):
    low = 0
    high = 1
    res = -1
    while(key>arr[high]):
        low=high
        high= 2 * high
    while(low<= high):
        mid = low+(high-low)//2
        if arr[mid]==key:
            res = mid
            high = mid-1
        elif arr[mid]>key:
            high - mid-1
        else:
            low = mid+1
    return res
arr = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1]
x= 1
print(index_first_in_infinite(arr , x))
