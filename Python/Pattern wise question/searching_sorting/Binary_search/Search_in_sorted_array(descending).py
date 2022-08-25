"""
problem : search an element in sorted array(descending order)
Ex : [8,7,6,5,4,3,2,1]
    x = 5
"""
def binary_search(arr , x , n):
    low = 0
    high = len(arr) -1

    while(low<=high):
        mid = low + (high-low)//2

        if (arr[mid]==x):
            return mid
        elif(arr[mid] > x):
            low = mid + 1
        else:
            high = mid - 1

arr=[8,7,6,5,4,3,2,1]
x = 5
n=len(arr)
res = binary_search(arr , x , n)
if(binary_search(arr , x , len(arr)) != -1):
    print(f"{x} is at index {str(res)}")
else:
    print("element not find")
