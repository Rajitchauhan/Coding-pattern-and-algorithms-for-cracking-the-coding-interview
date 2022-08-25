import heapq
from heapq import  heappush , heappop , heapify , heapreplace

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
class MinHeap:

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [[-i for i in val] for val in data]
            heapq.heapify(self.data)

    def top(self):
        return self.data[0]

    def push(self, item):
        heapq.heappush(self.data, item)

    def pop(self):
        return -heapq.heappop(self.data)

    def replace(self, item):
        return heapq.heapreplace(self.data, item)

def k_closest(arr , n , x, k):
    heap = MinHeap()

    for i in range(n):

        first = arr[i]-x
        second = i
        heap.push([first , second])
        print(heap.data)

arr= [10, 2, 14, 4, 7, 6]
k = 3
x = 4
n=len(arr)
print(k_closest(arr , n  ,x , k))
