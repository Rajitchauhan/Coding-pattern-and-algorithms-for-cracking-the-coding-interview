"""

Number of Distinct Islands
MediumAccuracy: 62.29%Submissions: 20K+Points: 4
Lamp
Land your Dream Job with Mega Job-a-thon. Register Now!

Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).

Example 1:

Input:
grid[][] = {{1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 0, 1, 1},
            {0, 0, 0, 1, 1}}
Output:
1
Explanation:
grid[][] = {{1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 0, 1, 1},
            {0, 0, 0, 1, 1}}
Same colored islands are equal.
We have 2 equal islands, so we
have only 1 distinct island.

Example 2:

Input:
grid[][] = {{1, 1, 0, 1, 1},
            {1, 0, 0, 0, 0},
            {0, 0, 0, 0, 1},
            {1, 1, 0, 1, 1}}
Output:
3
Explanation:
grid[][] = {{1, 1, 0, 1, 1},
            {1, 0, 0, 0, 0},
            {0, 0, 0, 0, 1},
            {1, 1, 0, 1, 1}}
Same colored islands are equal.
We have 4 islands, but 2 of them
are equal, So we have 3 distinct islands.

Your Task:

You don't need to read or print anything. Your task is to complete the function countDistinctIslands() which takes the grid as an input parameter and returns the total number of distinct islands.

Expected Time Complexity: O(n * m)
Expected Space Complexity: O(n * m)

Constraints:
1 ≤ n, m ≤ 500
grid[i][j] == 0 or grid[i][j] == 1


"""

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def bfs(self , r , c , vis , grid , row, col , lt):
        queue = deque()
        queue.append([r , c])
        vis[r][c] = 1
        
        while queue:
            r , c = queue.popleft()

            lt.append((r - row , c - col))

            directions = [[r+1 , c] , [r  , c+1] , [r-1,  c] , [r , c-1]]
            for i  , j in directions:
                if(i >= 0 and j >=0 and i < n and j < m and
                 vis[i][j] == 0 and grid[i][j] == 1
                ):
                    queue.append([i , j])
                    vis[i][j] = 1

    def dfs(self , r , c , vis , grid , lt , row , col):
        if( r >= len(grid) or r < 0 or c >= len(grid[0])
        or c < 0 or vis[r][c] == 1 or grid[r][c] == 0):
            return
        lt.append((r-row , c-col))
        vis[r][c] = 1

        directions = [[r-1 , c] , [r , c-1] , [r+1 , c] , [r , c+1]]
        for i , j in directions:
            self.dfs(i , j , vis , grid , lt , row , col)


    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        n , m = len(grid) , len(grid[0])

        vis = [[0 for j in range(m)]for i in range(n)]
        s = set()
        for i in range(n):
            for j in range(m):
                lt = []
                if vis[i][j] == 0 and grid[i][j] == 1:
                    self.dfs(i , j  , vis , grid, lt , i , j)
                    s.add(tuple(lt))
        return len(s)
