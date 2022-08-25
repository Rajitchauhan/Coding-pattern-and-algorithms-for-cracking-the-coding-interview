# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if(root == None):
            return res
        q = deque()
        q.append(root)

        while(q):
            sz = len(q)
            add = 0
            for i in range(sz):
                temp = q.popleft()
                add += temp.val

                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)

            res.append(add/sz)

        return res
        
