#include <iostream>
#include <vector>
bool solve(TreeNode* root , int sequence[] , i){
   if(!root) return false;

   if(i >= sequence.size() or root->val != sequence[i])
    return  false;
   if(!root->left and !root->right and i == sequence.size()-1)
    return true;

    return solve(root->left , sequence , i+1) or solve(root->right , sequence , i+1);
 }

bool fimdPath(TreeNode* root , sequence){
 if(!root) return sequence.empty();
 int index = 0
 return solve(root , sequence , index);
}
