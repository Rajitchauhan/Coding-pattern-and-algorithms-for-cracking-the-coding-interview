"""
problem :: next alphabet in sorted array.
Ex :: a,b,f,g => key = f
      ouput :: g
      a,b,f,h => key = f
      ouput :: h
"""
def next_alpha(arr , key , n):
    low , high=0,n-1
    res = -1

    while(low <= high):
        mid=low+(high-low)//2
        if arr[mid]==key:
            low =  mid+1
        elif arr[mid]>key:
            res = arr[mid]
            high = mid-1
        else:
            low = mid+1
    return res
arr=['a','b','f','g']
arr=['a','b','f','h']
key = 'f'
n=len(arr)
print(next_alpha(arr , key , n))
