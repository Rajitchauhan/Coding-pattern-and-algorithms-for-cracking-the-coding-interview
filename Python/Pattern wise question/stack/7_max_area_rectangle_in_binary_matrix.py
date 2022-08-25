"""
problem :: Max area rectangle in binary matrix.

Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s.

Example:

Input:
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
Output :
8
Explanation :
The largest rectangle with only 1's is from
(1, 0) to (2, 3) which is
1 1 1 1
1 1 1 1

Input:
0 1 1
1 1 1
0 1 1
Output:
6
Explanation :
The largest rectangle with only 1's is from
(0, 1) to (2, 2) which is
1 1
1 1
1 1


solution code (pass all test cases).

result = max_area_histogram(arr[0])
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):

            if (arr[i][j]):
                arr[i][j] += arr[i - 1][j]

        result = max(result, max_area_histogram(arr[i]))
    return result
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


def max_area_rectangle(arr):

    v1 = []
    for j in range(len(arr)):
        i=0
        v1.append(arr[i][j])
    Mx = max_area_histogram(v1)

    for i in range(1 , len(arr)):
        for j in range(0 , len(arr)):
            if arr[i][j]==0:
                v1[j] = 0
            else:
                v1[j] = v1[j] + arr[i][j]

        Mx = max(Mx , max_area_histogram(v1))
    return Mx

arr=  [[0 ,1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]]


arr = [[7, 2, 0 ,0 ],
       [1, 1, 1, 0],
       [1 ,0, 0, 1],
       [ 0, 1, 0, 1]]
print(max_area_rectangle(arr))
