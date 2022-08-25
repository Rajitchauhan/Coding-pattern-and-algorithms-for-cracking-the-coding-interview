
#Using min heap
import heapq
from heapq import heappop


# Function to find the k'th smallest element in a list using min-heap
def find_kth_smallest(input, k):

    # base case
    if not input or len(input) < k:
        exit(-1)

    # transform the input list into a min-heap
    heapq.heapify(input)

    # pop from min-heap exactly `k-1` times
    while k > 1:
        heappop(input)
        k = k - 1

    # return the root of min-heap
    return input[0]


if __name__ == '__main__':

    input = [7, 4, 6, 3, 9, 1]
    k = 3

    print('k\'th smallest element in the list is', find_kth_smallest(input, k))





#Using Max heap
import heapq


# A simple implementation of max-heap based on `heapq`
class MaxHeap:

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)

    def top(self):
        return -self.data[0]

    def push(self, item):
        heapq.heappush(self.data, -item)

    def pop(self):
        return -heapq.heappop(self.data)

    def replace(self, item):
        return heapq.heapreplace(self.data, -item)


# Function to find the k'th smallest element in a list using max-heap
def find_kth_smallest(input, k):

    # base case
    if not input or len(input) < k:
        exit(-1)

    # build a max-heap from the first `k` elements in the list
    pq = MaxHeap(input[0:k])

    # do for remaining list elements
    for i in range(k, len(input)):
        # if the current element is less than the root of the heap
        if input[i] < pq.top():
            # replace root with the current element
            pq.replace(input[i])

    # return the root of max-heap
    return pq.top()


if __name__ == '__main__':

    input = [7, 4, 6, 3, 9, 1]
    k = 3

    print('k\'th smallest element in the list is', find_kth_smallest(input, k))
