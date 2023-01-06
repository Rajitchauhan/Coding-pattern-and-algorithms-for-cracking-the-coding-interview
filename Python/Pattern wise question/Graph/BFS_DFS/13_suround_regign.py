"""
Replace O's with X's
MediumAccuracy: 34.0%Submissions: 25K+Points: 4
Given a matrix mat of size N x M where every element is either ‘O’ or ‘X’.
Replace all ‘O’ with ‘X’ that are surrounded by ‘X’.
A ‘O’ (or a set of ‘O’) is considered to be by surrounded by ‘X’ if there are ‘X’ at locations just below, just above, just left and just right of it.
Example 1:
Input: n = 5, m = 4
mat = {{'X', 'X', 'X', 'X'},
       {'X', 'O', 'X', 'X'},
       {'X', 'O', 'O', 'X'},
       {'X', 'O', 'X', 'X'},
       {'X', 'X', 'O', 'O'}}
Output: ans = {{'X', 'X', 'X', 'X'},
               {'X', 'X', 'X', 'X'},
               {'X', 'X', 'X', 'X'},
               {'X', 'X', 'X', 'X'},
               {'X', 'X', 'O', 'O'}}
Explanation: Following the rule the above
matrix is the resultant matrix.

Your Task:
You do not need to read input or print anything. Your task is to complete the function fill() which takes n, m and mat as input parameters ad returns a 2D array representing the resultant matrix.
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
Constraints:
1 ≤ n, m ≤ 500

"""

class Solution:
    def dfs(self , r , c , vis , mat):
        if r >= len(mat) or r < 0  or c < 0 or c >= len(mat[0]) or vis[r][c] == 1 or mat[r][c] == 'X':
            return

        vis[r][c] = 1

        self.dfs(r+1 , c , vis , mat)
        self.dfs(r , c+1 , vis , mat)
        self.dfs(r-1 , c , vis , mat)
        self.dfs(r , c-1 , vis , mat)
    def fill(self, n, m, mat):
        # code here
        vis = [[0 for j in range(m)]for i in range(n)]

        for j in range(m):
            # first col
            if mat[0][j] == 'O':
                self.dfs(0 , j  ,vis, mat)

            if mat[n-1][j] == 'O':
                self.dfs(n-1 , j , vis , mat)


        # first row

        for i in range(n):
            if mat[i][0] == 'O':
                self.dfs(i , 0 , vis , mat)

            if mat[i][m-1]== 'O':
                self.dfs(i , m-1 , vis , mat)


        for i  in range(n):
            for j in range(m):
                if vis[i][j] != 1:
                    mat[i][j] = 'X'

        return mat
