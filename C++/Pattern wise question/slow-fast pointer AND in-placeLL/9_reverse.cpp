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

      Node* reverseList(Node*);

 };

void Linkedlist:: printList(Node* head){
   Node* curr = head;
   cout<<"List :: "<<endl;
   while(curr){
    cout<<curr->data<< " ";
    curr = curr->next;
   }

}

Node* Linkedlist::reverseList(Node* head){
  Node* curr = head;
  Node* pre = NULL;
  Node* nxt = NULL;
  while(curr){
   nxt = curr->next;
   curr->next = pre;
   pre = curr;
   curr = nxt;
  }
  return pre;
 }

int main(){
 Node* newnode = new Node(1);
 newnode->next = new Node(2);
 newnode->next->next = new Node(3);
 newnode->next->next->next = new Node(4);
 newnode->next->next->next->next = new Node(5);

 Linkedlist obj;
 obj.printList(newnode);
 cout<<endl<<"After reverse list :: "<<endl;
 Node* res = obj.reverseList(newnode);
 while(res){
    cout<<res->data<<" ";
    res = res->next;
 }
return 0;
}
