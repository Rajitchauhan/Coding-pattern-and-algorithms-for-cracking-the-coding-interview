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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
       vector<vector<int>> res;
        if(root == NULL)
            return res;
        queue<TreeNode*> q;
        q.push(root);
        bool check = true;
        while(!q.empty()){
            int sz = q.size();
            vector<int> curr;
            for(int i=0; i<sz; i++){
                TreeNode* temp = q.front();
                q.pop();
                curr.push_back(temp->val);
                /*
                if(check){
                    curr[i] = temp->val;
                }
                else{
                    curr[sz - 1 - i] = temp->val;
                }

                */

                if(temp->left) q.push(temp->left);

                if(temp->right) q.push(temp->right);

            }
            if(check){
               res.push_back(curr);
            }
            else{
                reverse(curr.begin() , curr.end());
                res.push_back(curr);
            }
            //res.push_back(curr);            check = !check;
        }
        return res;
    }
};
