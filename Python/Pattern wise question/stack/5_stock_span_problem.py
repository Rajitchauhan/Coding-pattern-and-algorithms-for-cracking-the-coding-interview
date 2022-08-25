"""
problem :: Stock span problem is a financial problem mostly asked in interviews and
            its optimized solution can be obtained using stack.

Input:  [100, 80, 60, 70, 60, 75, 85]
Output: [ 1 , 1 , 1 , 2 , 1 ,  4 , 6]

Input: [31, 27, 14, 21, 30, 22]
Output:[ 1, 1 , 1 , 2 , 4 , 1]

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





def stock_span(arr):
    stack = Stack()
    vactor = []

    for i in range(len(arr)):
        if stack.isEmpty():
            vactor.append(-1)
            stack.push([arr[i] , i])
        elif not stack.isEmpty():
            while(not stack.isEmpty() and arr[i] >= stack.top()[0]):
                stack.pop()

            if stack.isEmpty():
                vactor.append(-1)
            else:
                vactor.append(stack.top()[1])

        stack.push([arr[i] , i])

    output = []
    for index , elements in enumerate(vactor):
        output.append(index-elements)
    return output


arr = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(arr))
