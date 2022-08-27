https://leetcode.com/problems/path-sum-ii

class Solution:
    def solve(self, root, S , curr , res):
        if(not root):
            return
        curr.append(root.val)


        if(root.val == S and not root.left and not root.right):
            res.append(list(curr))
            #remember that when append lisi of list convert into a list
        self.solve(root.left, S - root.val , curr , res)

        self.solve(root.right, S - root.val , curr , res)

        #del curr[-1]
        curr.pop()



    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        curr = []
        self.solve(root , targetSum , curr , res)
        return res
