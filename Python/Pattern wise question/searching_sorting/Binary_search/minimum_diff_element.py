"""
problem :: minimum difference between elements in sorted array.
Ex   ::   4,6,10 = > key = 7
output :: 6 BCZ {abs(4-7 = 3 , 6-7 = 1 , 10-7 = 3)}

Ex   ::   4,6,7,10 = > key = 7
output :: 7 BCZ {abs(4-7 = 3 , 6-7 = 1 ,7-7 = 0 , 10-7 = 3)}
"""


def left_neighbhor(arr , x , n):
    low , high = 0 , n-1
    res = -1
    while(low<=high):
        mid = low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high = mid-1
        else:
            res = mid
            low = mid+1
    return res

def right_neighbhor(arr , x , n):
    low , high = 0 , n-1
    res = -1
    while(low<=high):
        mid = low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            res = mid
            high = mid-1
        else:
            low = mid+1
    return res


def min_diff(arr , x):
    n=len(arr)
    i = left_neighbhor(arr , x , n)
    j = right_neighbhor(arr , x , n)
    if abs(x-arr[i]) < abs(x-arr[j]):
        return arr[i]
    elif abs(x-arr[i]) > abs(x-arr[j]):
        return arr[j]
    else:
        return arr[i]

arr= [4,6,10]
arr=[4,6,7,10]
arr= [4,6,6,10]
arr=[4,6,7,7,10]
x=7
print(min_diff(arr , x))
