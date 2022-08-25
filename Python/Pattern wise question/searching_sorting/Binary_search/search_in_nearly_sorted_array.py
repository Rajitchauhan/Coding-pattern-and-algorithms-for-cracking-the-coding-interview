"""
problem : search an element in nearly sorted array.
Ex :: Given array = [5 , 10 , 30 , 20 , 40]
    { ith element = (i-1) , i , (i+1) }
    sorted array  = [5 , 10 , 20 , 30 , 40]
"""

def search_in_nearly_sorted_array(arr , x , n):
    low , high = 0 , n-1
    while(low<=high):
        mid = low+(high-low)//2

        if (mid >= low and arr[mid-1]==x):
            return mid-1
        if (mid <= high and arr[mid+1]==x):
            return mid+1

        if (arr[mid]==x):
            return mid
        elif arr[mid] > x:
            high = mid-2
        else:
            low = mid+2

arr=[5 , 10 , 30 , 20 , 40]
x=40
n=len(arr)-1
print(search_in_nearly_sorted_array(arr ,x ,n))
