
/* Problem 2: Given a LinkedList with ‘n’ nodes,
 reverse it based on its size in the following way:

If ‘n’ is even, reverse the list in a group of n/2 nodes.
If n is odd, keep the middle node as it is,
 reverse the first ‘n/2’ nodes and reverse the last ‘n/2’ nodes.
Solution: When ‘n’ is even we can perform the following steps:

Reverse first ‘n/2’ nodes: head = reverse(head, 1, n/2)
Reverse last ‘n/2’ nodes: head = reverse(head, n/2 + 1, n)
When ‘n’ is odd, our algorithm will look like:

head = reverse(head, 1, n/2)
head = reverse(head, n/2 + 2, n)
Please note the function call in the second step.
 We’re skipping two elements as we will be skipping the middle element.

*/


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

      Node* reverseSubList(Node* , int , int);

 };

void Linkedlist:: printList(Node* head){
   Node* curr = head;
   cout<<"List :: "<<endl;
   while(curr){
    cout<<curr->data<< " ";
    curr = curr->next;
   }
}

Node* Linkedlist::reverseSubList(Node* head , int p , int q){
  if(p == q)
    return head;
  Node* curr = head;
  Node* pre = NULL;
  for(int i=0; i<p-1 && curr != nullptr; i++){
   pre = curr;
   curr = curr->next;
  }
  Node* lastNodeofFirstList = pre;
  Node* lastNodeofSubList = curr;

  Node* nxt = NULL;
  for(int i=0; i< q-p+1 && curr != nullptr; i++){
    nxt = curr->next;
    curr->next = pre;
    pre = curr;
    curr = nxt;
  }
  if(lastNodeofFirstList != NULL){
    lastNodeofFirstList->next = pre;
  }
  else{
    head = pre;
  }
  lastNodeofSubList->next = curr;
  return head;
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
 Node* res = obj.reverseSubList(newnode , 2 , 4);
 while(res){
    cout<<res->data<<" ";
    res = res->next;
 }
return 0;
}


