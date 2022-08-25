# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if(root == None):
            return res
        queue = deque()
        queue.append(root)

        while(queue):
            no = len(queue)
            curr = []
            for _ in range(no):
                tmp = queue.popleft()

                curr.append(tmp.val)

                if(tmp.left):
                    queue.append(tmp.left)

                if(tmp.right):
                    queue.append(tmp.right)
            res.append(curr)


        return res
        
