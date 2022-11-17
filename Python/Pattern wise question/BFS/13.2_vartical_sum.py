"""

Vertical sum
EasyAccuracy: 64.76%Submissions: 23943Points: 2
Given a Binary Tree,
find vertical sum of the nodes that are in same vertical line.
Print all sums through different vertical lines starting from left-most vertical line to right-most vertical line.
Example 1:
Input:
      1
    /   \
  2      3
 / \    / \
4   5  6   7
Output:
Explanation:
The tree has 5 vertical lines
Vertical-Line-1 has only one node
4 => vertical sum is 4
Vertical-Line-2: has only one node
2=> vertical sum is 2
Vertical-Line-3: has three nodes:
1,5,6 => vertical sum is 1+5+6 = 12
Vertical-Line-4: has only one node 3
=> vertical sum is 3
Vertical-Line-5: has only one node 7
=> vertical sum is 7

Your Task:
You don't need to take input.
 Just complete the function verticalSum()
  that takes root node of the tree as parameter and returns an array containing the vertical sum of tree from left to right.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1<=Number of nodes<=1000

"""
from collections import deque
class Solution:
    def verticalSum(self, root):

        mp ={}
        res = []
        if not root:
            return res

        queue = deque()
        queue.append([root , 0])

        while queue:

            sz = len(queue)

            for i in range(sz):

                temp , freq = queue.popleft()

               # if freq  in mp:
                if freq in mp:
                    mp[freq] =mp[freq]  + temp.data
                else:
                    mp[freq] = temp.data


                if temp.left:
                    queue.append([temp.left , freq-1])

                if temp.right:
                    queue.append([temp.right , freq+1])

        for k , v in sorted(mp.items()):
            res.append(v)

        return res
