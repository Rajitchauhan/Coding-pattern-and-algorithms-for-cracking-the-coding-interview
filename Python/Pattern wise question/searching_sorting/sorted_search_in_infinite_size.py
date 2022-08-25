"""
problem :: you have a sorted array which size is infinite ,
         your task is to find x element in this array

"""

def binary_search(arr ,low  , high ,  x):
    while low <= high:

        mid = (low + high) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

def No_size_sorted(arr , x):
    low = 0
    high = 1
    val = arr[0]
    while(val < len(arr) and val < x):
        low = high
        high = 2*high
        val = arr[high]

    return binary_search(arr , low , high , x)

arr = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,21,22,23,24,25,26,31,32,33,34,35,36,37]
x = 13

result  = No_size_sorted(arr , x)
if result != -1:
    print(f"x is at  index {str(result)}")
else:
    print(f"x element is not  found")


"""
def binary_search(arr,l,r,x):

    if r >= l:
        mid = l+(r-l)//2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binary_search(arr,l,mid-1,x)

        return binary_search(arr,mid+1,r,x)

    return -1

def findPos(a, key):

    l, h, val = 0, 1, arr[0]

    # Find h to do binary search
    while val < key:
        l = h            #store previous high
        h = 2*h          #double high index
        val = arr[h]       #update new val

    # at this point we have updated low and high indices,
    # thus use binary search between them
    return binary_search(a, l, h, key)

# Driver function
arr = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,21,22,23,24,25,26,31,32,33,34,35,36,37]
ans = findPos(arr,15)
if ans == -1:
    print ("Element not found")
else:
    print("Element found at index",ans)
"""
