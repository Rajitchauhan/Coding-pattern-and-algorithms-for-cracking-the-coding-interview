"""
problem :: search in Bitonic array.
Ex :: 1 , 3  , 8 , 12 , 4 , 2 => 4
output  :: 4 at index
"""

def asc_binary(arr ,low , high , x):

    while(low <= high):
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high = mid-1
        else:
            low = mid +1
    return -1

def desc_binary(arr ,low , high , x):

    while(low <= high):
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            low = mid +1
        else:
            high = mid-1
    return -1




def peak(arr , low , high ,n):

    while(low <= high):
        mid=low+(high-low)//2
        if mid==0:
            if arr[mid]>=arr[mid+1]:
                return mid
            else:
                return  mid+1
        elif mid==(n-1):
                if arr[mid]>arr[mid-1]:
                    return mid
                else:
                    return mid-1
        else:
            if (arr[mid]>arr[mid-1] and arr[mid]> arr[mid+1]):
                return mid
            elif arr[mid]>arr[mid-1]:
                low=mid+1
            else:
                high = mid-1
    return -1

def search_in_bitonic(arr , x,index , n):
    if x > arr[index]:
        return -1
    elif x == arr[index]:
        return index
    else:
        i = asc_binary(arr , 0 , index-1 , x)
        if i != -1:
            return i

        desc_binary(arr, index+1, n-1 , x)


def main():
    #arr=[1 , 3 , 5, 8 ,10]
    #arr=[10 , 8 ,5 , 3  ,  1]
    arr = [1 , 3  , 8 , 12 , 4 , 2]
    x=4
    n=len(arr)
    low = 0
    high = n-1
    index = peak(arr , low , high , n)
    result = search_in_bitonic(arr , x, index , n)
    if result != -1:
        print(f"element is at {result}")
    else:
        return -1

main()

"""

# Python code to search key in bitonic array

# Function for binary search in ascending part
def ascendingBinarySearch(arr, low, high, key):

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    return -1

# Function for binary search in descending part of array
def descendingBinarySearch(arr, low, high, key):

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            high = mid - 1
        else:
            low = mid + 1

    return -1

# Find bitonic point
def findBitonicPoint(arr, n, l, r):

    bitonicPoint = 0
    mid = (r + l) // 2

    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return mid

    elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
        bitonicPoint = findBitonicPoint(arr, n, mid, r)
    else:
        bitonicPoint = finsBitonicPoint(arr, n, l, mid)

    return bitonicPoint

# Function to search key in bitonic array
def searchBitonic(arr, n, key, index):

    if key > arr[index]:
        return -1
    elif key == arr[index]:
        return index
    else:
        temp = ascendingBinarySearch(arr, 0, index-1, key)
        if temp != -1:
            return temp

        # search in right of k
        return descendingBinarySearch(arr, index+1, n-1, key)

# Driver code
def main():
    arr = [1 , 3  , 8 , 12 , 4 , 2]
    key = 4
    n = len(arr)
    l = 0
    r = n - 1

    # Function call
    index = findBitonicPoint(arr, n, l, r)

    x = searchBitonic(arr, n, key, index)

    if x == -1:
        print("Element Not Found")
    else:
        print("Element Found at index", x)

main()

"""
