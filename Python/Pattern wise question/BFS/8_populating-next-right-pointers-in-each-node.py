"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
"""
This problem follows the Binary Tree Level Order Traversal pattern.
We can follow the same BFS approach.
The only difference is that while traversing a level we will remember the previous node to connect it with the current node.


so we will connect at each level
for that will take prevous = None
and instead of inserting we will check
if(prevous != None):
    pre.next = current # current is equal queue.popleft()
pre = current # at first time to connect

at the end
we will return root
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if(not root):
            return None
        q = deque()
        q.append(root)

        while(q):
            sz = len(q)
            pre = None
            for i in range(sz):
                curr = q.popleft()
                if(pre != None):
                    pre.next = curr
                pre = curr
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)

        return root
