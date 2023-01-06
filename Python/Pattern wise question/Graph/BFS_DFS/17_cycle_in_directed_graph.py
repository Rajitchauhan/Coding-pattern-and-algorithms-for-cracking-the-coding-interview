"""

Detect cycle in a directed graph
MediumAccuracy: 27.88%Submissions: 241K+Points: 4
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.

Example 1:
Input:



Output: 1
Explanation: 3 -> 3 is a cycle

Example 2:
Input:


Output: 0
Explanation: no cycle in the graph

Your task:
You dont need to read input or print anything. Your task is to complete the function isCyclic() which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the given directed graph contains a cycle or not.

Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)

Constraints:
1 ≤ V, E ≤ 105
"""


class Solution:

    #Function to detect cycle in a directed graph.
    def dfs(self , node , vis , visPath , adj):

        vis[node] = 1
        visPath[node] = 1

        for child in  adj[node]:
            if vis[child] == 0:
                if(self.dfs(child , vis , visPath , adj)) == True:
                    return True
            elif vis[child] == 1 and visPath[child] == 1:
                return True
        visPath[node] = 0
        return False

    def isCyclic(self, V, adj):
        # code here
        vis = [0]*V
        visPath = [0]*V

        for i in range(V):
            if vis[i] == 0:
                if (self.dfs(i , vis , visPath , adj)) == True:
                    return True

        return False

@ using Topological sort

from collections import deque
class Solution:

    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        degree = [0]*V

        for i in range(V):
            for child in adj[i]:
                degree[child] += 1

        queue = deque()
        for i in range(V):
            if degree[i] == 0:
                queue.append(i)
        cnt = 0
        while queue:
            node = queue.popleft()
            cnt += 1

            for child in adj[node]:
                degree[child] -= 1
                if degree[child] == 0:
                    queue.append(child)

        if cnt == V:
            return False
        else:
            return True

            
