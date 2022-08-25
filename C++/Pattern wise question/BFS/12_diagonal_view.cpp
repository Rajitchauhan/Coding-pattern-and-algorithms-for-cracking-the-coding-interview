vector<int> diagonal(Node *root)
{
   // your code here
   vector<int> res;
   if(!root) return res;
   queue<Node*> q;
   q.push(root);
   while(!q.empty()){
       Node* temp = q.front();
       q.pop();
       while(temp){
           if(temp->left){
               q.push(temp->left);
           }
           res.push_back(temp->data);
           temp = temp->right;
       }

   }
   return res;
}
