"""
problem :: find position of an element in infinte array.
Ex  ::  1,2,3,4,5,6,7,8,9,10.................infinte.
        x = 8.
"""

def searach_infinite(arr , key):
    low = 0
    high = 1
    #val = arr[0]
    while(key > arr[high]):
        low=high
        high = 2 * high
        #val = arr[high]
    while(low<= high):
        mid = low + (high-low)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            high= mid-1
        else:
            low=mid+1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,33,34,35]
x=13
print(searach_infinite(arr , x))
