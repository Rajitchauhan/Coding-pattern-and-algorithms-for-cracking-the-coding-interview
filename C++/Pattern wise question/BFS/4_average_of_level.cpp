class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        if(root == NULL)
            return res;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int sz = q.size();
            double sum=0;
            for(int i=0; i<sz; i++){
                 TreeNode* temp = q.front();
                 q.pop();
                 sum += temp->val;

                if(temp->left) q.push(temp->left);

                if(temp->right) q.push(temp->right);

            }
            res.push_back(sum / sz);
        }
        return res;
    }
};
