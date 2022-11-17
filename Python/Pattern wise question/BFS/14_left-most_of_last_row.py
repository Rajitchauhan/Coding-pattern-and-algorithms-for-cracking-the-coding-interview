"""

Given the root of a binary tree,
return the leftmost value in the last row of the tree.



Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = deque()
        q.append(root)
        if not root.left and not root.right:
            return root.val
        while q:

            sz = len(q)
            res = []
            for _ in range(sz):
                temp = q.popleft()
                res.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

        return res[0]



class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = deque()
        q.append(root)
        if not root.left and not root.right:
            return root.val
        while q:

            sz = len(q)
            res = 0
            #res = []
            for i in range(sz):
                temp = q.popleft()
                #res.append(temp.val)
                if i == 0:
                    res = temp.val
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)


        return res
