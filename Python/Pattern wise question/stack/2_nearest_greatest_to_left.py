"""
problem :: Nearest Greater to left.
Ex ::   [1 ,3  , 2 , 4]
output ::[-1 , -1 , 3 , -1]

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
            raise Exception("underfloe")
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.stack[-1]


def greatest_nearest_left(arr):
    stack = Stack()
    vactor = []
    for i  in range(len(arr)):
        if stack.isEmpty():
            vactor.append(-1)
            stack.push(arr[i])
        elif not stack.isEmpty():
            while(not stack.isEmpty() and arr[i] > stack.top()):
                stack.pop()
            if stack.isEmpty():
                vactor.append(-1)
            else:
                vactor.append(stack.top())
        stack.push(arr[i])
    return vactor

arr =[1 ,3  , 2 , 4]
print(greatest_nearest_left(arr))
