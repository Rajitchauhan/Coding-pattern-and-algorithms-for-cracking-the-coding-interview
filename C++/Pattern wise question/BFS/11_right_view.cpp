
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if(!root) return res;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int sz = q.size();
            for(int i=0;  i<sz; i++){
                TreeNode* temp = q.front();
                q.pop();
                if(i == sz-1) res.push_back(temp->val);

                if(temp->left) q.push(temp->left);

                if(temp->right) q.push(temp->right);
            }
        }
        return res;
    }
};
