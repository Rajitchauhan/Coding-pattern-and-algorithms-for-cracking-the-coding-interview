"""
problem : find ceil of an element in sorted array.
Ex : 1,2,3,4,5,6,7,8,9,10,10,12,19 => x = 7
     output :  {7}

Ex : 1,2,3,4,5,8,9,10,10,12,19 => x = 7
     output : {8} BCZ it is greater then 7 and smaller than other min([8,9,10,10,10,12,19])

"""
def ceil(arr , x  ,n):
    low , high = 0,n-1
    res=-1
    while(low <= high):
        mid=low+(high-low)//2
        if arr[mid]==x:
            return arr[mid]
        elif arr[mid]>x:
            res =  arr[mid]
            high = mid-1
        else:
            low=mid+1
    return res
#arr = [1,2,3,4,5,6,7,8,9,10,10,12,19]
arr = [ 1,2,3,4,5,8,9,10,10,12,19]
x=7
n=len(arr)
print(ceil(arr , x , n))
