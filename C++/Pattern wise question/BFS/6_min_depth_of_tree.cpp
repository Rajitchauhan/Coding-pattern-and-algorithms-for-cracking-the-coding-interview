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
    int minDepth(TreeNode* root) {
        int minDepth = 0;
        if(root == NULL)
            return minDepth;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int sz = q.size();
            minDepth += 1;
            for(int i=0; i<sz; i++){
                TreeNode* temp = q.front();
                q.pop();

                if(temp->left == NULL and temp->right == NULL){
                    return minDepth;
                }

                if(temp->left) q.push(temp->left);

                if(temp->right) q.push(temp->right);
            }
        }
        return minDepth;
    }
};

// second using DFS

class Solution {
public:
     bool flag = false;
    int minDepth(TreeNode* root) {
        if (!root) {
            if (flag) return INT_MAX;
            return 0;
        }
        flag = true;
        if (!root->left && !root->right) return 1;
        return 1 + min(minDepth(root->left), minDepth(root->right));
    }
};
