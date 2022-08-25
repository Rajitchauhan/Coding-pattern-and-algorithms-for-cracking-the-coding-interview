#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
class Solution:
    def diagonal(self,root):
        #:param root: root of the given tree.
        #return: print out the diagonal traversal,  no need to print new line
        #code here
        res = []
        if(not root):
            return res
        q =  deque()
        q.append(root)
        while(q):
            temp = q.popleft()
            while(temp):
                if(temp.left):
                    q.append(temp.left)
                res.append(temp.data)
                temp = temp.right

        return res
