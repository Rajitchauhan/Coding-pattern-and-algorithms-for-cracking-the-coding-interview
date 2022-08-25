"""
problem : kth smallest element
arr = [7, 4, 6, 3, 9, 1]
k = 3

Output:

k’th smallest array element is 4
"""
import heapq

class Maxheap:
    def __init__(self , data=None):
        if data is None:
            self.data=[]
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)

    def push(self , items):
        heapq.heappush(self.data , -items)

    def top(self):
        return -self.data[0]

    def pop(self):
        return -heapq.heappop(self.data)

    def replace(self , items):
        return heapq.heapreplace(self.data , -items)


def find_kth_smallest(arr , k):
    if not arr or len(arr) < k:
        exit(-1)
    heap = Maxheap(arr[0:k])

    for i in range(k , len(arr)):
        if arr[i] < heap.top():
            heap.replace(arr[i])

    return heap.top()

if __name__ == '__main__':

    arr = [7, 4, 6, 3, 9, 1]
    k = 3

    print('k\'th smallest element in the list is', find_kth_smallest(arr, k))
