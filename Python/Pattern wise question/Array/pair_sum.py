"""
input = [1,2,4,2,6,22,70,3,5,72,23,45,64]
k = 10
output = 4 , 6
"""

def pair_sum(arr , n , k):
    n = len(arr)
    k = 28
    arr = sorted(arr)
    i , j = 0, 1
    while i < n and j < n:
        if i != j and arr[j] + arr[i] == k:
            return arr[i] , arr[j]
        elif arr[i] + arr[j] < k:
            j += 1
        else:
            i += 1
    return False

arr = [1,2,4,2,6,22,70,3,5,72,23,45,64]
k = 28
n = len(arr)
print(pair_sum(arr , n , k))
