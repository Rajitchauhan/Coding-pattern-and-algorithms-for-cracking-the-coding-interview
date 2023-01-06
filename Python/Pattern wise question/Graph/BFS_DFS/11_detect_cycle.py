Detect cycle in an undirected graph
MediumAccuracy: 30.13%Submissions: 237K+Points: 4

Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.
Example 1:
Input:
V = 5, E = 5
adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}}
Output: 1
Explanation:

1->2->3->4->1 is a cycle.

Example 2:
Input:
V = 4, E = 2
adj = {{}, {2}, {1, 3}, {2}}
Output: 0
Explanation:

No cycle in the graph.


Your Task:
You don't need to read or print anything. Your task is to complete the function isCycle() which takes V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the undirected graph contains any cycle or not, return 1 if a cycle is present else return 0.
NOTE: The adjacency list denotes the edges of the graph where edges[i] stores all other vertices to which ith vertex is connected.

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)


Constraints:
1 ≤ V, E ≤ 105

@ usng BFS

from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    def bfs(self , sr , vis , adj):
        vis[sr] = 1

        queue = deque()
        queue.append([sr , -1])

        while queue:

            node , parent = queue.popleft()

            for child in adj[node]:
                if vis[child] == 0:
                    vis[child] = 1
                    queue.append([child , node])
                elif child != parent:
                    return True
        return False

	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis = [0]*V

		for i in range(V):
		    if vis[i] == 0:
		        if self.bfs(i , vis , adj) :
		            return True

		return False


@ using DFS

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.

    def dfs(self , node , parent , vis , adj):
        vis[node] = 1
        for child in adj[node]:
            if vis[child] == 0:

                if self.dfs(child , node , vis , adj):
                    return True
            elif parent != child:
                return True
        return False

	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis = [0]*V

		for i in range(V):
		    if vis[i] == 0:
		        if self.dfs(i  , -1, vis , adj):
		            return True
		return False
