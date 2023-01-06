
"""


Find the number of islands
MediumAccuracy: 42.12%Submissions: 132K+Points: 4


Given a grid of size n*m (n is the number of rows and m is the
number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.

Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or
 vertically or diagonally i.e., in all 8 directions.
Example 1:
Input:
grid = {{0,1},{1,0},{1,1},{1,0}}
Output:
1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.

Example 2:
Input:
grid = {{0,1,1,1,0,0,0},{0,0,1,1,0,1,0}}
Output:
2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 1 0
There are two islands :- one is colored in blue
and other in orange.

Your Task:
You don't need to read or print anything.
Your task is to complete the function numIslands()
which takes the grid as an input parameter and returns the total number of islands.
Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)
Constraints:
1 ≤ n, m ≤ 500


"""





@leetcode solution

class Solution:

    def bfs(self , grid , vis , row , col):
        n  , m = len(grid)  , len(grid[0])

        queue = []
        queue.append([row , col])

        while queue:

            temp = queue.pop(0)
            print(temp)
            row = temp[0]
            col = temp[1]
            lt = [[row , col+1] , [row+1 , col] , [row-1 , col] , [row , col-1]]
            for i , j in lt:
                if i < n and j < m and i >=0 and j >=0 and vis[i][j] == 0 and grid[i][j] == '1':
                    queue.append([i , j])
                    vis[i][j] = 1

    def numIslands(self,grid):
        #code
        n , m = len(grid) , len(grid[0])

        vis = [[0 for j in range(m)] for i in range(n)]
        count =0
        for r  in range(n):
            for c in range(m):
                if vis[r][c] == 0 and grid[r][c] == '1':
                    count += 1
                    self.bfs(grid , vis , r , c)

        return count

@GFG solution
class Solution:

    def bfs(self , grid , vis , row , col):
        n  , m = len(grid)  , len(grid[0])
        #vis[row][col] = 1
        queue = []
        queue.append([row , col])

        while queue:
            #temp = queue.pop(0)
            temp = queue.pop(0)
            #print(temp)
            row = temp[0]
            col = temp[1]
            lt = [[row , col+1] , [row+1 , col] , [row-1 , col]
            , [row , col-1]
            , [row-1 , col-1] , [row-1 , col+1] , [row+1 , col+1] ,[row+1 , col-1]]
            for i , j in lt:
                if i < n and j < m and i >=0 and j >=0 and vis[i][j] == 0 and grid[i][j] == 1:
                    queue.append([i , j])
                    vis[i][j] = 1



    def numIslands(self,grid):
        #code
        n , m = len(grid) , len(grid[0])

        vis = [[0 for j in range(m)] for i in range(n)]
        count =0
        for r  in range(n):
            for c in range(m):
                if vis[r][c] == 0 and grid[r][c] == 1:
                    count += 1
                    self.bfs(grid , vis , r , c)

        return count
