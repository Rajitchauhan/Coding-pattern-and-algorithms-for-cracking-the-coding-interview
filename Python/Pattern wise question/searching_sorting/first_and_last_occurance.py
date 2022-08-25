"""
problem : find first and last occurence in sorted array

Ex : [1,2,2,2,3,4,7,8]
    x = 2
output : first occurence =  1 ,last occurence =  3

"""

def firstOcc(arr , x , n):
    low= 0
    high = n-1
    res = -1
    while(low<=high):
        mid = low + (high-low)//2
        if arr[mid]==x:
            res = mid
            high = mid-1
        elif(arr[mid]>x):
            high = mid -1
        else:
            low = mid+1
    return res

def lastOcc(arr , x , n):
    low= 0
    high = n-1
    res = -1
    while(low<=high):
        mid = low + (high-low)//2
        if arr[mid]==x:
            res = mid
            low = mid+1
        elif(arr[mid]>x):
            high = mid -1
        else:
            low = mid+1
    return res


arr=[1,2,2,2,3,4,7,8]
x=2
n=len(arr)

print(firstOcc(arr , x , n))
print(lastOcc(arr , x , n))
