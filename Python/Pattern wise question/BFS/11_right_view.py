class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if(not root):
            return res
        q = deque()
        q.append(root)

        while(q):
            sz = len(q)
            for i in range(sz):
                curr = q.popleft()
                if(i == sz-1):
                    res.append(curr.val)
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
        return res
        
