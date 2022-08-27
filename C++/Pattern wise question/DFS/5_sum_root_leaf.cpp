https://leetcode.com/problems/sum-root-to-leaf-numbers/
class Solution {
public:
    int solve(TreeNode* root  , int sum){
        if(!root) return 0;

        sum = sum*10 + root->val;
        if(!root->left and !root->right){
            return sum;
        }
        return solve(root->left , sum) + solve(root->right  , sum);

    }
    int sumNumbers(TreeNode* root) {
        int sum=0;
        return solve(root , sum);

    }
};
