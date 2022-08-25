"""
problem :: sort a k sorted array or sort nearly sorted array.
Ex :: [6 , 5 , 3 , 2 , 8 , 10 , 9]
 k :: 3
 element exits at (i+k) or (i-k). i.e : 6 should be (i+k)or(i-k) {4 index right or may be left}
"""

import heapq
from heapq import heappop, heappush


# Function to sort a k–sorted array
def sort_k_sorted_arr(arr, k):

    # build a min-heap from the first `k+1` elements in the list
    min_heap = arr[0:k+1]
    heapq.heapify(min_heap)

    # do for remaining elements in the list
    index = 0
    for i in range(k+1, len(arr)):

        # pop the top element from the min-heap and assign them to the
        # next available list index
        arr[index] = heappop(min_heap)
        index = index + 1

        # push the next list element into min-heap
        heappush(min_heap, arr[i])

    # pop all remaining elements from the min-heap and assign them to the
    # next available list index
    while min_heap:
        arr[index] = heappop(min_heap)
        index = index + 1


if __name__ == '__main__':

    arr = [6 , 5 , 3 , 2 , 8 , 10 , 9]
    k = 3

    sort_k_sorted_arr(arr, k)
    print(arr)
