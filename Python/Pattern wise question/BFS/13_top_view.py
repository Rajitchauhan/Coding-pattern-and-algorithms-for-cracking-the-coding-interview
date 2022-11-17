"""

Top View of Binary Tree
MediumAccuracy: 38.43%Submissions: 100k+Points: 4
Given below is a binary tree.
 The task is to print the top view of binary tree.
 Top view of a binary tree is the set of nodes visible when the tree is viewed from the top
  For the given below tree
   	1
	/ 	\
   2   	3
  /  \	/   \
4	5  6   7
Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node.
Example 1:
Input:
      1
   /	\
  2  	3
Output: 2 1 3

Example 2:
Input:
       10
    /  	\
  20  	  30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100

Your Task:
Since this is a function problem.
 You don't have to take input.
  Just complete the function topView()
  that takes root node as parameter and returns a list of nodes visible from the top view from left to right.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N).
Constraints:
1 ≤ N ≤ 105
1 ≤ Node Data ≤ 105

"""
from collections import deque
class Solution:

    #Function to return a list of nodes visible from the top view
    #from left to right in Binary Tree.
    def topView(self,root):

        # code here

        mp = {}
        res = []
        if not root:
            return res

        queue = deque()

        queue.append([root , 0])

        while queue:

            sz = len(queue)

            curr = 0

            for i in range(sz):

                temp , freq = queue.popleft()

                if freq not in mp:
                    mp[freq] = temp.data

                if temp.left:
                    queue.append([temp.left , freq-1])

                if temp.right:
                    queue.append([temp.right , freq+1])

        for k , v in sorted(mp.items()):
            res.append(v)

        return res
