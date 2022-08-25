# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if(root == None):
            return res

        q = deque()
        q.append(root)
        check = True
        while(q):
            sz = len(q)
            curr = []
            for i in range(sz):
                temp = q.popleft()

                curr.append(temp.val)

                if(temp.left):
                    q.append(temp.left)

                if(temp.right):
                    q.append(temp.right)

            if(check):
                res.append(curr)
            else:
                res.append(curr[::-1])

            check = not check

        return res
        
