"""
problem :  Nearest smaller to left.
Ex ::     [4 , 5 , 2 , 10 , 8]
output :: [-1 , 4 , -1 ,2 , 2]
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
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.stack[-1]


def smallest_to_left(arr):
    stack =Stack()
    vactor = []
    for i in range(len(arr)):
        if stack.isEmpty():
            vactor.append(-1)
            stack.push(arr[i])
        elif not stack.isEmpty():
            while(not stack.isEmpty() and arr[i] < stack.top()):
                stack.pop()
            if stack.isEmpty():
                vactor.append(-1)
            else:
                vactor.append(stack.top())
        stack.push(arr[i])

    return vactor

arr = [4 , 5 , 2 , 10 , 8]
print(smallest_to_left(arr))
