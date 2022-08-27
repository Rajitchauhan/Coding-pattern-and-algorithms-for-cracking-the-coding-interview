https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    def solve(self , root  , s):
        if(not root): return 0;
        s = s*10 + root.val
        if(not root.left and not root.right):
            return s
        return self.solve(root.left , s) + self.solve(root.right  , s)


    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        return self.solve(root, 0)
        
