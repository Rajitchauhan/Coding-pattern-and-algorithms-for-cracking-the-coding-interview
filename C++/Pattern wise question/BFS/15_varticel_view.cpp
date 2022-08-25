987. Vertical Order Traversal of a Binary Tree
Hard

4110

3618

Add to List

Share
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:


class Solution {
public:

    vector<vector<int>> verticalTraversal(TreeNode* root) {
        map<int, map<int, multiset<int>>> nodes;
        queue<pair<TreeNode *, pair<int, int>>> todo;
        todo.push({root,{0,0}}); // initial vertical and level
        while (!todo.empty())
        {
            auto p = todo.front();
            todo.pop();
            TreeNode *temp = p.first;

            // x -> vertical , y->level
            int x = p.second.first, y = p.second.second;
            nodes[x][y].insert(temp->val); // inserting to multiset

            if (temp->left)
            {
                todo.push({temp->left,{x - 1 , y + 1}});
            }
            if (temp->right)
            {
                todo.push({temp->right,{x + 1 , y + 1}});
            }
        }
        vector<vector<int>> ans;
        for (auto p : nodes) //vertical
        {
            vector<int> col;
            for (auto q : p.second)  //p.second==map<int, multiset<int>>
            {
                col.insert(col.end(), q.second.begin(), q.second.end()); //inserting multiset nodes in level at the last position
            }
            ans.push_back(col);
        }
        return ans;
    }
};

// if you liked the solution then please upvote it so that it can reach to more people
// If you have any doubt or want to discuss any thing related to solution please leave a com


Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
