"""

Course Schedule
MediumAccuracy: 51.77%Submissions: 12K+Points: 4

Land your Dream Job with Mega Job-a-thon. Register Now!
There are a total of n tasks you have to pick, labeled from 0 to n-1. Some tasks may have prerequisites tasks, for example to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]
Given the total number of n tasks and a list of prerequisite pairs of size m. Find a ordering of tasks you should pick to finish all tasks.
Note: There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all tasks, return an empty array. Returning any correct order will give the output as 1, whereas any invalid order will give the output 0.

Example 1:
Input:
n = 2, m = 1
prerequisites = {{1, 0}}
Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible order is [0, 1].
Example 2:
Input:
n = 4, m = 4
prerequisites = {{1, 0},
                 {2, 0},
                 {3, 1},
                 {3, 2}}
Output:
1
Explanation:
There are a total of 4 tasks to pick.
To pick task 3 you should have finished
both tasks 1 and 2. Both tasks 1 and 2
should be pick after you finished task 0.
So one correct task order is [0, 1, 2, 3].
Another correct ordering is [0, 2, 1, 3].
Returning any of these order will result in
a Output of 1.


Your Task:
The task is to complete the function findOrder() which takes two integers n, and m and a list of lists of size m*2 denoting the prerequisite pairs as input and returns any correct order to finish all the tasks. Return an empty array if it's impossible to finish all tasks.

Constraints:
1 ≤ n ≤ 104
0 ≤ m ≤ 105
0 ≤ prerequisites[0], prerequisites[1] ≤ 105
All prerequisite pairs are unique
prerequisites[0] ≠ prerequisites[1]

Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(n+m).
"""
from collections import defaultdict , deque
class Solution:
    def findOrder(self, V, m, prerequisites):
        # Code here
        adj = defaultdict(list)
        inDegree = [0]*V
        for parent , child in prerequisites:
            adj[child].append(parent)
            inDegree[parent] += 1
        """
        degree = [0]*V

        for i in range(V):
            for child in adj[i]:
                degree[child] += 1
        """


        queue = deque()

        for i in range(V):
            if inDegree[i] == 0:
                queue.append(i)

        topo = []

        while queue:
            node = queue.popleft()

            topo.append(node)

            for child in adj[node]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child)


        if(len(topo) == V):
            return topo
        else:
            return []
