https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self , root , res , s ):
        if(not root): return

        if(not root.left and not root.right):
            s += str(root.val)
            res.append(s)
        s += str(root.val) + "->"

        self.solve(root.left , res , s)
        self.solve(root.right , res , s)


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        s = ""
        self.solve(root , res , s)
        return res
