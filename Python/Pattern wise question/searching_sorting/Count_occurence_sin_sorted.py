"""
problem : count occurences an element in sorted array.
Ex : [2 , 4 , 10 , 10 , 10 , 18 , 20]
     x = 10
output : 3 times

formula = (last occurence - first occurence) + 1
"""
def Count(arr , first , last):
    i =firstOcc(arr , x , n)
    if i==-1:
        return i
    j = lastOcc(arr , x , n)
    return (j-i)+1

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

arr=[2 , 4 , 10 , 10 , 10 , 18 , 20]
x=10
n=len(arr)

print(Count(arr , x , n))
