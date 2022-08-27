https://leetcode.com/problems/path-sum-ii/submissions/

class Solution {
public:
    void solve(TreeNode* root, int sum ,vector<vector<int>>& res ,
        vector<int> &curr ){
        if(!root) return;

        curr.push_back(root->val);

        if(root->val == sum and !root->left and !root->right){
            res.push_back(curr);
        }

        solve(root->left, sum - root->val , res ,curr );

        solve(root->right, sum - root->val , res ,curr );

        curr.pop_back();

    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> res;
        vector<int> curr;
        solve(root , targetSum , res , curr);
        return res;

    }
};



class Solution {
public:
    void path(TreeNode* root, int k , vector<int> arr , vector<vector<int>> &res , int sum) {

        if(!root) return;
        sum = sum+root->val;
        arr.push_back(root->val);
        if(root->left==NULL and root->right==NULL)
            if(sum==k){
                res.push_back(arr);
                return;
            }
        path(root->left , k , arr , res , sum);
        path(root->right , k , arr , res, sum);

    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {

        vector<vector<int>> res;
        if(!root) return res;
        vector<int> arr;
        path(root , targetSum , arr , res,0);
        return res;
    }
};
