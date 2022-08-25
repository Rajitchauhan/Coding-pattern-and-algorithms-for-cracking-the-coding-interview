#include <iostream>
using namespace std;

class TreeNode{
   public:
    TreeNode* data;
    TreeNode* left;
    TreeNode* right;
    TreeNode * root;

   };
 TreeNode* BST:: insert(Node*node , int val){
        if(node==NULL){
         node = new Tree;
         node->data = val;
         node->left = NULL;
         node->right = NULL;
         node->parent= NULL;
        }

    }
void Tree::Inorder(Node* root){
    cout<<"this is going to print tree Node in inorder"<<endl;
 }
int main(){
   TreeNode* root = NULL;
   root = insert(root , 1);
   root = insert(root , 2);
   root = insert(root , 3);

 return 0;
}
/*
class Tree{
   public:
       Tree(){
        Node* root=NULL;
       }
    void insert

   };

void Tree::Inorder(Node* root){
    cout<<"this is going to print tree Node in inorder"<<endl;
 }


 */
