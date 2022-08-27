https://leetcode.com/problems/binary-tree-paths/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void solve(TreeNode* root ,  vector<string> & res ,  string s){
        if(!root) return;



        if(!root->left and !root->right){
            s += to_string(root->val);
            res.push_back(s);
        }

        s +=  to_string(root->val) +"->" ;

        solve(root->left ,  res ,  s);

        solve(root->right ,  res ,  s);
        s.pop_back();
    }
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        string s= "";
        solve(root , res , s);
        return res;
    }
};
