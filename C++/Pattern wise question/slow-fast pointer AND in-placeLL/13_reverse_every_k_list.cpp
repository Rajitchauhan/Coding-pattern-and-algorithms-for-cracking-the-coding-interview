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

      Node* reverseSubList(Node* , int);

 };

void Linkedlist:: printList(Node* head){
   Node* curr = head;
   cout<<"List :: "<<endl;
   while(curr){
    cout<<curr->data<< " ";
    curr = curr->next;
   }
}

Node* Linkedlist::reverseSubList(Node* head , int k){
    if( k <= 1 or head == NULL)
        return head;

    Node* curr=head;
    Node* pre=NULL;
    while(true){
        Node* lastnodeofFirstList = pre;
        Node* lastnodeofsublist = curr;

        Node* nxt=NULL;
        for(int i=0; i<k && curr != NULL; i++){
            nxt = curr->next;
            curr->next = pre;
            pre = curr;
            curr = nxt;
        }
        if(lastnodeofFirstList != nullptr){
            lastnodeofFirstList->next = pre;
        }
        else{
           head =  pre;
        }
        lastnodeofsublist->next = curr;

        if(curr == nullptr){
            break;
        }
        pre = lastnodeofsublist;
    }
    return head;
 }

int main(){
 Node* newnode = new Node(1);
 newnode->next = new Node(2);
 newnode->next->next = new Node(3);
 newnode->next->next->next = new Node(4);
 newnode->next->next->next->next = new Node(5);
 newnode->next->next->next->next->next = new Node(6);
 newnode->next->next->next->next->next->next = new Node(7);
 newnode->next->next->next->next->next->next->next = new Node(8);

 Linkedlist obj;
 obj.printList(newnode);
 cout<<endl<<"After reverse list :: "<<endl;
 Node* res = obj.reverseSubList(newnode , 2);
 while(res){
    cout<<res->data<<" ";
    res = res->next;
 }
return 0;
}


