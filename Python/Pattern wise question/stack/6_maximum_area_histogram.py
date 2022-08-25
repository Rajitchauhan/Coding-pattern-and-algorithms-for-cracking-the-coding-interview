"""
problem ::  Find the largest rectangular area possible in a given histogram where
            the largest rectangle can be made of a number of contiguous bars.
            Assume that all bars have same width and the width is 1 unit.

 Given n non-negative integers representing the histogram's bar height
 where the width of each bar is 1, find the area of largest rectangle in the histogram.

 Ex :: Input: [2, 1, 5, 6, 2, 3]
       Output: 10

       Input: [6, 2, 5, 4, 5, 1, 6]
       Output: 12
"""
from collections import deque
class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self , items):
        self.stack.append(items)

    def isEmpty(self):
        return len(self.stack)==0

    def pop(self):
        if self.isEmpty():
            raise Exception("underflow")
        return  self.stack.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

def nearest_smaller_left(arr):
    stack = Stack()
    vactor = []
    for i in range(len(arr)):
        if stack.isEmpty():
            vactor.append(-1)
            stack.push([arr[i] , i])
        elif not stack.isEmpty():
            while(not stack.isEmpty() and arr[i] <= stack.top()[0]):
                stack.pop()
            if stack.isEmpty():
                vactor.append(-1)
            else:
                vactor.append(stack.top()[1])
        stack.push([arr[i] , i])

    return vactor

def nearest_smaller_right(arr):
    stack=Stack()
    vactor = []
    for i in range(len(arr)-1 , -1 ,-1):
        if stack.isEmpty():
            vactor.append(len(arr))
            stack.push([arr[i] , i])
        elif not stack.isEmpty():
            while(not stack.isEmpty() and arr[i] <= stack.top()[0]):
                stack.pop()
            if stack.isEmpty():
                vactor.append(len(arr))
            else:
                vactor.append(stack.top()[1])
        stack.push([arr[i] , i])
    vactor.reverse()
    return vactor

def max_area_histogram(arr):
    right = nearest_smaller_right(arr)
    left = nearest_smaller_left(arr)

    width = []

    for i in range(len(arr)):
        width.append(right[i]-left[i]-1)

    area = []
    for i in range(len(arr)):
        area.append(arr[i]*width[i])

    return max(area)

arr = [6, 2, 5, 4, 5, 1, 6]
print(max_area_histogram(arr))



"""

OPTIMIZE SOLUTION : SILIGHTY different


class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack Underflow')
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

def max_area_histogram(arr):
    stack = Stack()
    stack.push(-1)
    max_area = 0

    for i in range(len(arr)):
        while stack.peek() != -1 and arr[stack.peek()] >= arr[i]:
            last_element_index = stack.pop()
            max_area = max(max_area, arr[last_element_index] * (i - stack.peek() - 1))
        stack.push(i)

    while stack.peek() != -1:
        last_element_index = stack.pop()
        max_area = max(max_area, arr[last_element_index] * (len(arr) - stack.peek() - 1))

    return max_area

arr = [6, 2, 5, 4, 5, 1, 6]

print(max_area_histogram(arr))
