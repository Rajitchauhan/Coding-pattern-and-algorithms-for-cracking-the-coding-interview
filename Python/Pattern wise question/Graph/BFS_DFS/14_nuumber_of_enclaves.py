1020. Number of Enclaves
Medium
2K
39
Companies
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.



Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.



class Solution:
    def dfs(self , r , c ,vis , grid):
        if r < 0 or r >= len(grid) or c < 0 or c  >= len(grid[0]) or vis[r][c] == 1 or grid[r][c] == 0:
            return

        vis[r][c] = 1
        self.dfs(r+1 , c , vis , grid)
        self.dfs(r , c+1 , vis , grid)
        self.dfs(r-1 , c , vis , grid)
        self.dfs(r , c-1 , vis , grid)
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])

        vis = [[0 for j in range(m)] for i in range(n)]

        # first col

        for j in range(m):
            if grid[0][j] == 1:
                self.dfs(0 , j , vis , grid)

            if grid[n-1][j] == 1:
                self.dfs(n-1  , j  , vis  , grid)

        for i in range(n):
            if grid[i][0] == 1:
                self.dfs(i , 0 , vis , grid)

            if grid[i][m-1] == 1:
                self.dfs(i  , m-1 , vis ,  grid)
        print("after")
        print(vis)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    cnt += 1

        """
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 1:
                    grid[i][j] = 0
        print("grid")
        print(grid)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1
        """
        return cnt
