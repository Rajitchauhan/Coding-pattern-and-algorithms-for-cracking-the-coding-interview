#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <stack>
#include <map>
#include <utility>
using namespace std;
struct Node{
  int data;
  Node*left , *right;

  Node(int val){
    data = val;
    left = NULL;
    right = NULL;
  }
};

void inOrder(Node* root){
  if(root==nullptr) return;
  inOrder(root->left);
  cout<<root->data<<" ";
  inOrder(root->right);
 }

void postOrder(Node* root){
  if(root==NULL) return;
  postOrder(root->left);
  postOrder(root->right);
  cout<<root->data<<" ";
}
int height(Node* root){
  if(root==NULL) return 0;
  return 1+max(height(root->left) , height(root->right));

}

void preOrder(Node* root){
  if(root==NULL) return;
  cout<<root->data<<" " ;
  preOrder(root->left);
  preOrder(root->right);
}
void levelOrder(Node* root){
    queue<Node*> q;
    if(root==NULL) return;
    q.push(root);

    while(!q.empty()){
        Node* temp = q.front();
        cout<<temp->data<<" ";
        q.pop();
        if(temp->left) q.push(temp->left);
        if(temp->right) q.push(temp->right);
    }

}
void revLevel(Node*root){
 queue<Node*> q;
 if(root==nullptr) return;
 q.push(root);
 while(!q.empty()){
    Node* temp = q.front();
    cout<<temp->data<<" ";
    q.pop();
    if(temp->right) q.push(temp->right);
    if(temp->left) q.push(temp->left);

 }
}

void bottomLevel(Node*root){
 vector <int> v;
 queue<Node*> q;
 if(!root) return;
 q.push(root);
 while(!q.empty()){
    Node*temp = q.front();
    v.push_back(temp->data);
    q.pop();
    if(temp->right) q.push(temp->right);
    if(temp->left) q.push(temp->left);
 }

  reverse(v.begin() , v.end());
 for(int i: v)
    cout<<i<<" ";
}

void SumOflevelOrder(Node* root){
    queue<Node*> q;
    if(root==NULL) return;
    q.push(root);
    int sum=0;
    while(!q.empty()){
        Node* temp = q.front();
        //cout<<temp->data<<" ";
        sum =sum + temp->data;
        q.pop();
        if(temp->left) q.push(temp->left);
        if(temp->right) q.push(temp->right);
    }
  cout<<"sum is :: "<<sum<<endl;
}
void levelSum(Node* root){
    queue<Node*> q;
    if(root==NULL) return;
    q.push(root);

    while(!q.empty()){
      int sz  = q.size();
      int sum = 0;
      for(int i =0;i<sz;i++){
        Node* temp = q.front();
        sum = sum+temp->data; //output :: 1 5 9
        q.pop();
        if(temp->left) q.push(temp->left);
        if(temp->right) q.push(temp->right);
      }
      cout<<"Level sum "<<sum<<" ";

    }

}
void RecLeftView(Node* root){

  if(!root) return;

  if(root->left)
     RecLeftView(root->left);
    cout<<root->data<<" ";
 }

void leftview(Node* root){
 queue<Node*> q;
 if(!root) return;
 q.push(root);
// int sum=0;
 while(!q.empty()){
    int sz = q.size();
    for(int i=0; i<sz; i++){
        Node* temp = q.front();
        q.pop();
        if(i==0)
           cout<<temp->data<<" ";
          // sum += temp->data; for sum of left view
        if(temp->left) q.push(temp->left);
        if(temp->right) q.push(temp->right);
    }
 }
 //cout<<"sum of leftview is ::  "<<sum;
}
void rightview(Node* root){
 queue<Node*> q;
 if(!root) return;
 q.push(root);
 while(!q.empty()){
    int sz = q.size();
    for(int i=0; i<sz; i++){
        Node* temp = q.front();
        q.pop();
        if(i==0)
            cout<<temp->data<<" ";
        if(temp->right) q.push(temp->right);
        if(temp->left) q.push(temp->left);
    }
 }
}

 void topview(Node *root) {
        map<int,int> m;
        queue<pair<Node*,int>>q;
        q.push({root,0});
        while(!q.empty()){
            auto a = q.front();
            q.pop();
            Node* node = a.first;
            int hd = a.second;
           // int val = a.second;
            //int v = mp[val];
            //mp[val]= v + curr->data; // sum of vertical(top) view
            if(m.count(hd)==0)
                m[hd] = node->data;

            if(node->left)q.push({node->left, hd-1});
            if(node->right)q.push({node->right, hd+1});
        }
        // vector<int>res;
        for(auto it: m){
            cout<<(it.second)<<" ";
        }
    }

void bottomview(Node *root) {
        map<int,int> m;
        queue<pair<Node*,int>>q;
        q.push({root,0});
        while(!q.empty()){
            auto a = q.front();
            q.pop();
            Node* node = a.first;
            int hd = a.second;

                m[hd] = node->data;

            if(node->left)q.push({node->left, hd-1});
            if(node->right)q.push({node->right, hd+1});
        }
        for(auto it: m){
            cout<<(it.second)<<" ";
        }
    }


  void daigonalview(Node* root){
   queue<Node*> q;
   //if(!root) return;
   q.push(root);
   while(!q.empty()){
    Node* tmp = q.front();
    q.pop();
    while(tmp){

        if(tmp->left)
            q.push(tmp->left);
        cout<<tmp->data<<" ";
        tmp = tmp->right;
    }
   }

   }
void daigonalsum(Node*root){
 queue<Node*> q;
 q.push(root);
 while(!q.empty()){
    Node* temp = q.front();
    q.pop();
    int sum=0;
    while(temp){
        if(temp->left)
            q.push(temp->left);
        //cout<<temp->right<<" ";
        sum = sum+temp->data;
        temp=temp->right;
    }
    cout<<sum<<" ";

 }

}

int main(){

  Node* root = new Node(1);
 // cout<<root->data<<" " <<endl;
  root->left = new Node(2);
  root->right = new Node(3);
  root->left->left = new Node(4);
  root->left->right = new Node(5);
  //root-> = new Node(2);
  //Tree t = new Tree();
  // TRAVERSE IN DFS
  /*
  cout<<"Inoder :: "<<endl;
  inOrder(root);
  cout<<endl;
  cout<<"Postorder :: "<<endl;
  postOrder(root);
  cout<<endl;
  cout<<"Preorder :: "<<endl;
  preOrder(root);
  cout<<"Height :: ";
  int h = height(root);
  cout<<h<<endl;


  cout<<"Level order ::"<<endl;
  levelOrder(root);
  cout<<endl;
  cout<<"rLevel order ::"<<endl;
  revLevel(root);
  cout<<endl;
  cout<<"Bottom (Reverse)Level order ::"<<endl;
  bottomLevel(root);
 //  try some operation.
 cout<<endl;
 SumOflevelOrder(root);
 cout<<endl;
 levelSum(root);

 RecLeftView(root);
 cout<<endl;
 cout<<"Left View ::  ";
 leftview(root);
 cout<<endl;
 cout<<"right View ::  ";
 rightview(root);
 cout<<endl;

 cout<<"Top view :: ";
 topview(root);
 cout<<endl;

 cout<<"Bottom view :: ";
 bottomview(root);
*/
//cout<<"Diagonal view :: "<<endl;
//daigonalview(root);
//cout<<"Diagonal view sum :: "<<endl;
//daigonalsum(root);


 cout<<endl;
   levelSum(root);
 return 0;
}

