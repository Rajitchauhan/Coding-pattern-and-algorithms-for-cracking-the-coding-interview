"""
Bipartite Graph
MediumAccuracy: 31.25%Submissions: 96K+Points: 4
Given an adjacency list of a graph adj  of V no. of vertices having 0 based index. Check whether the graph is bipartite or not.
Example 1:
Input:

Output: 1
Explanation: The given graph can be colored
in two colors so, it is a bipartite graph.

Example 2:
Input:

Output: 0
Explanation: The given graph cannot be colored
in two colors such that color of adjacent
vertices differs.


Your Task:
You don't need to read or print anything. Your task is to complete the function isBipartite() which takes V denoting no. of vertices and adj denoting adjacency list of the graph and returns a boolean value true if the graph is bipartite otherwise returns false.

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)

Constraints:
1 ≤ V, E ≤ 105

"""
class Solution:
    def dfs(self  , node , col , vis , adj):
        vis[node] = col
        for child in adj[node]:
            if vis[child] == -1:
                if self.dfs(child , not col , vis , adj) == False:
                    return False
            elif vis[child] == col:
                return False

        return True
	def isBipartite(self, V, adj):
		#code here
		vis = [-1]*V
		for i in range(V):
		    if vis[i]  == -1:
		        if self.dfs(i , 0 , vis ,adj) == False:
		            return False
		return True
