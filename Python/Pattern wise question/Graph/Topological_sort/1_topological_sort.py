"""

Topological sort
MediumAccuracy: 56.52%Submissions: 118K+Points: 4
Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

Example 1:
Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 3, 2, 1, 0.

Example 2:
Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 5, 4, 2, 1, 3, 0.

Your Task:
You don't need to read input or print anything. Your task is to complete the function topoSort()  which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns an array consisting of a the vertices in Topological order. As there are multiple Topological orders possible, you may return any of them. If your returned topo sort is correct then console output will be 1 else 0.

Expected Time Complexity: O(V + E).
Expected Auxiliary Space: O(V).

Constraints:
2 ≤ V ≤ 104
1 ≤ E ≤ (N*(N-1))/2

"""
@ using dfs with stack
class Solution:

    #Function to return list containing vertices in Topological order.
    def dfs(self , node , vis , adj , st):
        vis[node] = 1

        for child in adj[node]:
            if vis[child] == 0:
                self.dfs(child, vis , adj , st)
        st.append(node)
    def topoSort(self, V, adj):
        # Code here
        st = []
        vis = [0]*V

        for i in range(V):
            if vis[i] == 0:
                self.dfs(i , vis , adj , st)
        res = []
        while st:
            res.append(st.pop())

        return res



from collections import deque
class Solution:

    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        inDegree = [0]*V

        for i in range(V):
            for child in adj[i]:
                inDegree[child] += 1

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

        return topo
