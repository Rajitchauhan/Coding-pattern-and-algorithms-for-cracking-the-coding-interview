"""
Input:

arr = [7, 4, 6, 3, 9, 1]
k = 2

Output:

The 2nd largest array element is 7
"""
import heapq
from heapq import heappop

def kth_largest(arr , k):
    if not arr and len(arr) > k:
        exit(-1)
    min_heap = arr[0:k]
    heapq.heapify(min_heap)

    for i in range(k , len(arr)):
        if arr[i] > min_heap[0]:
            heapq.heapreplace(min_heap , arr[i])

    return min_heap[0]

arr = [7, 4, 6, 3, 9, 1]
k = 2
print(kth_largest(arr , k))
