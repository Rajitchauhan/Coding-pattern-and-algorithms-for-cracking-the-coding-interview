
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
      //deque<vector<int>> res =   deque<vector<int>>();
     vector<vector<int>> res;
      if(root == NULL){
          return res;
      }

      queue<TreeNode*> q;
      q.push(root);
      while(!q.empty()){
          int no = q.size();
          vector<int> curr;
          for(int i=0; i<no; i++){
              TreeNode* temp = q.front();
              q.pop();
              curr.push_back(temp->val);
              if(temp->left) q.push(temp->left);

              if(temp->right) q.push(temp->right);
          }
          res.push_back(curr);

      }
        reverse(res.begin() , res.end());
        return res;
    }
};

Reverse Level Order Traversal
EasyAccuracy: 47.34%Submissions: 82990Points: 2
Given a binary tree of size N,
 find its reverse level order traversal.
  ie- the traversal must begin from the last level.

Example 1:

Input :
        1
      /   \
     3     2

Output: 3 2 1
Explanation:
Traversing level 1 : 3 2
Traversing level 0 : 1

Reverse Level Order Traversal
EasyAccuracy: 47.34%Submissions: 82990Points: 2
Given a binary tree of size N, find its reverse level order traversal. ie- the traversal must begin from the last level.

Example 1:

Input :
        1
      /   \
     3     2

Output: 3 2 1
Explanation:
Traversing level 1 : 3 2
Traversing level 0 : 1

