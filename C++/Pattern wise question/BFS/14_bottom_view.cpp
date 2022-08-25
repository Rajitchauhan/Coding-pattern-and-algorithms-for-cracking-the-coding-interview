
class Solution {
  public:
    vector <int> bottomView(Node *root) {
        // Your Code Here
        //Your code here
        vector<int> res;
        if(!root) return res;
        map<int , int> mp;
        queue<pair<Node* , int>> q;
        q.push({root , 0});
        while(!q.empty()){
            int sz = q.size();
            for(int i=0; i<sz; i++){
                auto temp =q.front();
                q.pop();
                Node* node = temp.first;
                int hd = temp.second;
                mp[hd] = node->data;

                if(node->left)  q.push({node->left , hd-1});

                if(node->right) q.push({node->right , hd+1});
            }

        }
        for(auto i:mp){
            res.push_back(i.second);
        }
        return res;

    }
};
