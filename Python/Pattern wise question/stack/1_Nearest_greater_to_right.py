"""
problem :: Nearest Greater to Right.
Ex ::    1,3,2,4
output : 3,4,4,-1


#Brute force
def nearest_right(arr):
    lt = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]<arr[j]:
                lt.append(arr[j])
                break
        else:
            lt.append(-1)
    return lt

arr = [1,3,2,4]
"""

#Using Stack
from collections import deque

class Stack:
  def __init__(self):
    self.stack = deque()

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

def nearest_greater_right(arr):
  stack = Stack()
  vactor = []

  for i in range(len(arr)-1, -1, -1):
    if stack.isEmpty():
      vactor.append(-1)
      stack.push(arr[i])
    elif not stack.isEmpty():
      while(not stack.isEmpty() and arr[i] > stack.peek()):
        stack.pop()
      if stack.isEmpty():
        vactor.append(-1)
      else:
        vactor.append(stack.peek())
      stack.push(arr[i])

  vactor.reverse()
  return vactor

arr = [11, 13, 21, 3]



arr = [1,3,2,4]
print(nearest_greater_right(arr))
