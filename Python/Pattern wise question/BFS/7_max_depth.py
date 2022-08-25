# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxiDepth = 0
        if(not root):
            return maxiDepth
        q = deque()
        q.append(root)
        while(q):
            sz = len(q)
            maxiDepth += 1
            for i in range(sz):
                temp = q.popleft()

                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
        return maxiDepth
