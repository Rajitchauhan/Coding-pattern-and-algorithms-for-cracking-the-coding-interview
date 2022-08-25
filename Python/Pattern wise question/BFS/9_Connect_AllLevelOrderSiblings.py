class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if(not root):
            return None
        q = deque()
        q.append(root)
        pre = None
        while(q):
            sz = len(q)

            for i in range(sz):
                curr = q.popleft()
                if(pre != None):
                    pre.next = curr
                pre = curr
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)

        return root
