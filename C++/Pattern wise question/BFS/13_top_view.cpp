
/*
struct Node
{
    int data;
    Node* left;
    Node* right;
};
*/
class Solution
{
    public:
    //Function to return a list of nodes visible from the top view
    //from left to right in Binary Tree.
    vector<int> topView(Node *root)
    {
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
                if(mp.count(hd) == 0){
                    mp[hd] = node->data;
                }
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
