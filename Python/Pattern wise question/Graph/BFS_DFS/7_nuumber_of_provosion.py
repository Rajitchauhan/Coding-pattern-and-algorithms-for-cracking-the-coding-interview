"""
Number of Provinces
MediumAccuracy: 54.29%Submissions: 30K+Points: 4

Bag Offers from Top Product Companies. Explore Exclusive Problems Now!
Given an undirected graph with V vertices. We say two vertices u and v belong to a single province if there is a path from u to v or v to u. Your task is to find the number of provinces.

Note: A province is a group of directly or indirectly connected cities and no other cities outside of the group.
Example 1:
Input:
[
 [1, 0, 1],
 [0, 1, 0],
 [1, 0, 1]
]

Output:
2
Explanation:
The graph clearly has 2 Provinces [1,3] and [2]. As city 1 and city 3 has a path between them they belong to a single province. City 2 has no path to city 1 or city 3 hence it belongs to another province.

Example 2:
Input:
[
 [1, 1],
 [1, 1]
]

Output :
1


Your Task:
You don't need to read input or print anything. Your task is to complete the function numProvinces() which takes an integer V and an adjacency matrix adj as input and returns the number of provinces. adj[i][j] = 1, if nodes i and j are connected and adj[i][j] = 0, if not connected.

Expected Time Complexity: O(V2)
Expected Auxiliary Space: O(V)

Constraints:
1 ≤ V ≤ 500

"""
@ solution
#User function Template for python3
from collections import defaultdict

class Solution:
    def numProvinces(self, adj, V):

        # make adj to adj list than simply traverse though bfs and count how many times the call of bfs is happens in serching for vis[i]==0 simple :) --

        nadj=[[]]

        for i in range(len(adj)):

            c=[]

            for j in range(len(adj[i])):

                if(adj[i][j]==1 and j!=i):

                    c.append(j+1)

            nadj.append(c)

        vis=[0]*(V+1)

        c1=0

        from collections import deque

        def bfs(i):
            q=deque([])
            q.append(i)
            vis[i]=1
            while(len(q)!=0):
                cur=q.popleft()
                for j in nadj[cur]:
                    if(vis[j]==0):
                        vis[j]=1
                        q.append(j)
        for i in range(1,V+1):
            if(vis[i]==0):
                c1=c1+1
                bfs(i)
        return c1




@ Solution 2
#User function Template for python3
from collections import defaultdict

class Solution:
    def numProvinces(self, adj, V):

        # make adj to adj list than simply traverse though bfs and count how many times the call of bfs is happens in serching for vis[i]==0 simple :) --

        nadj=[[]]

        for i in range(len(adj)):

            c=[]

            for j in range(len(adj[i])):

                if(adj[i][j]==1 and j!=i):

                    c.append(j+1)

            nadj.append(c)

        vis=[0]*(V+1)

        c1=0

        from collections import deque

        def bfs(i):

            q=deque([])

            q.append(i)

            vis[i]=1

            while(len(q)!=0):

                cur=q.popleft()

                for j in nadj[cur]:

                    if(vis[j]==0):

                        vis[j]=1

                        q.append(j)

        for i in range(1,V+1):

            if(vis[i]==0):

                c1=c1+1

                bfs(i)
        return c1


@ leetcode
from collections import defaultdict
class Solution:
    def convert(self ,adj):
        adjList = defaultdict(list)
        n = len(adj)
        for i in range(n):
            for j in range(i+1 , n):
                if adj[i][j] == 1:
                    adjList[i].append(j)
                    adjList[j].append(i)
        return adjList
    def dfs(self , node , adjList , vis):
        vis[node] = True
        for child in adjList[node]:
            if vis[child] == False:
                self.dfs(child , adjList , vis)

    def findCircleNum(self, adj: List[List[int]]) -> int:
        n = len(adj)
        vis = [False]*n
        adjList = self.convert(adj)
        print(adjList)
        ans = 0
        for i in range(n):
            if vis[i] == False:
                ans += 1
                self.dfs(i , adjList , vis)
        return ans
