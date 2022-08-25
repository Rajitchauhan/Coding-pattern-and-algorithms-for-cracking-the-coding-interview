class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return 1+ max(self.minDepth(root.left), self.minDepth(root.right))
        return 1+ min(self.minDepth(root.left), self.minDepth(root.right))


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        minDepth  =  0
        if not root:
            return minDepth
        q = deque()
        q.append(root)
        while(q):
            sz = len(q)
            minDepth += 1
            for i in range(sz):
                temp = q.popleft()
                if(not temp.left and not temp.right):
                    return minDepth
                if(temp.left):
                    q.append(temp.left)

                if(temp.right):
                    q.append(temp.right)

        return minDepth


class Solution:
    check = False
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            if(self.check):
                return  sys.maxsize
            return 0
        self.check = True
        if not root.left and not root.right:
            return 1
        return 1+ min(self.minDepth(root.left), self.minDepth(root.right))
