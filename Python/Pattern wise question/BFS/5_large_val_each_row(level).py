class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if(root == None):
            return res
        q = deque()
        q.append(root)

        while(q):
            sz = len(q)
            MIN_INT = -sys.maxsize - 1
            mini = MIN_INT
            for i in range(sz):
                temp = q.popleft()
                mini = max(mini , temp.val)
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)

            res.append(mini)

        return res
