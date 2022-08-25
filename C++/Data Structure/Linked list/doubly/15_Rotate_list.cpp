#include <iostream>

using namespace std;

class Node{
   public:
   int data;
   Node* next;

   Node(int data){
    this->data = data;
    this->next = NULL;
   }
 };

class Linkedlist{
  Node* head;
  public:
      Linkedlist() { head = NULL; }

      void printList(Node*);

      Node* rotateList(Node* , int);

 };

void Linkedlist:: printList(Node* head){
   Node* curr = head;
   cout<<"List :: "<<endl;
   while(curr){
    cout<<curr->data<< " ";
    curr = curr->next;
   }
}

Node* Linkedlist::rotateList(Node* head , int r){
  if(head != NULL or head->next != NULL or r <= 0){
    return head;
  }
  int len=0;
  Node* curr = head;
  Node*  pre = NULL;
  while(curr){
    len += 1;
    pre = curr;
    curr = curr->next;
  }
  pre->next = head;
  r = r % len;
  if(r == 0) return head;
  int skip_list = len - r;

  for(int i=0; i < skip_list; i++){
    pre = head;
    head = head->next;
  }
  pre->next = NULL;

  return head;
 }

int main(){
 Node* newnode = new Node(1);
 newnode->next = new Node(2);
 newnode->next->next = new Node(3);
 newnode->next->next->next = new Node(4);
 newnode->next->next->next->next = new Node(5);
 newnode->next->next->next->next->next = new Node(6);

 Linkedlist obj;
 obj.printList(newnode);
 cout<<endl<<"After reverse list :: "<<endl;
 Node* res = obj.rotateList(newnode  , 3);
 while(res){
    cout<<res->data<<" ";
    res = res->next;
 }
return 0;
}

