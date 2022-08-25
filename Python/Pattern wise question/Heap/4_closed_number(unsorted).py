
import heapq

class maxHeap:
    def __init__(self , data=None):
        if data is None:
            self.data=[]
        else:
            self.data = [[-i for i in val] for val in data]
            heapq.heapify(self.data)

    def push(self , items):
        heapq.heappush(self.data , -items)

    def top(self):
        return -self.data[0]

    def pop(self):
        return -heapq.heappop(self.data)

    def replace(self , items):
        return heapq.heapreplace(self.data , -items)


def k_closest(arr , n , x, k):
    max_heap = maxHeap()

    for i in range(n):
        first = abs(arr[i]-x)
        second = i
        max_heap.push([first , second])

        if len(max_heap) > k:
            max_heap.pop()

    while(len(max_heap) > 0):
        print(max_heap.top())
        max_heap.pop()



arr= [10, 2, 14, 4, 7, 6]
k = 3
x = 4
n=len(arr)
print(k_closest(arr , n  ,x , k))

"""


"""
