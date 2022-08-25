#include <iostream>
// recursive function to print list
// insert any pos and delete any position(for future revision).
using namespace std;

class Node{
 public:
    int data;
    Node* next;

    // i can skip.
    Node(){
     data = 0;
     next = NULL;
    }


    Node(int data){
     this->data = data;
     this->next = NULL;
    }
};

class Linkedlist{
  Node* head;
  public:
  Linkedlist(){ head  = NULL; }

  void insertBeg(int);

  void insertEnd(int);

  int listLen();

  void insertAny(int , int); // *

  void printList();

  void printListRec(Node*);

  void deleteNode();

  void deletePos(int); // *


};


void Linkedlist::insertBeg(int data){
  Node* curr = head;
  //cout<<"insert in begining"<<endl;
  Node* newnode = new Node(data);
    newnode->data = data;
    newnode->next = NULL;
  if(curr == NULL){
    head = newnode;
  }
  else{
    newnode->next = head;
    head = newnode;
  }

}

void Linkedlist::insertEnd(int data){
  Node* curr = head;
  Node* newnode = new Node(data);
  newnode->data = data;
  newnode->next = NULL;
 // cout<<"insert at end"<<endl;
  if(curr==NULL){
   // insertBeg(data);
   head = newnode;
  }
  else{
    while(curr != NULL){
        curr = curr->next;
    }
    curr->next = newnode;
  }
 }

int Linkedlist::listLen(){
  int count=0;
  Node* curr=head;
  if(head==NULL){
    cout<<"list length is "<<count<<endl;
  }
  while(curr){
    count++;
    curr = curr->next;
  }
  cout<<"list length is "<<count<<endl;
}

void Linkedlist::printList()
     {

    Node* curr = head;

    // Check for empty list.
    if (curr == NULL) {
        cout << "List empty" << endl;
        return;
    }

    // Traverse the list.
    while (curr != NULL) {
        cout << curr->data << "-> "<<endl;
        curr = curr->next;
     }
    }
 void Linkedlist:: printListRec(Node* head){
    if(head==NULL || head->next==NULL){
        return;
    }
    cout<<head->data<<"  ";
    printListRec(head->next);
   }



void Linkedlist::deleteNode(){
 Node* curr = head;
 if(curr==NULL){
    cout<<"list have no element"<<endl;
    return;
 }
 else{
    head = curr->next;
    delete curr;
    return;
 }


}

void Linkedlist::insertAny(int pos , int data){

  Node* newnode = new Node(data);
  newnode->data = data;
  newnode->next = NULL;
  if(head==NULL){
   // insertBeg(data);
    newnode->next = NULL;
    head = newnode;
  }
  if(pos < 0 and pos >= listLen()){
    cout<<"invalid position"<<endl;
    return;
  }

  Node* curr=head;
  for(int i=0; i<pos-1 ; i++){
    curr = curr->next;
  }
  newnode->next = curr->next;
  curr->next = newnode;


}

void Linkedlist::deletePos(int pos){
  if(pos < 0 and pos >= listLen()){
    cout<<"Invalid position :: "<<endl;
    return;
  }
  Node* curr = head;

  if(head->next==NULL){
    curr = head;
    head = NULL;
    delete curr;
  }

  for(int i=0; i<pos-1; i++){
    curr = curr->next;
  }
  Node* nxt = curr->next->next;
  delete curr->next;
  //free(curr->next);
  curr->next = nxt;
}

int main(){
  Node* newnode = new Node(10);
 //cout<<newnode->data<<" "<<endl;
 Linkedlist obj;
 obj.insertBeg(20);
 obj.insertBeg(30);
 obj.insertBeg(40);
 obj.insertBeg(50);
 obj.insertBeg(60);
 obj.insertBeg(70);
 obj.insertBeg(80);
 cout<<"Length of linked list :: "<<obj.listLen();
 cout<<"Printing a linked list "<<endl;
 //obj.printListRec(???..); logic is write
 //obj.printList();
 //obj.insertAny(2 , 100);
 //obj.printList();
 //cout<<"after delete staring node"<<endl;
 //obj.deleteNode();
 //obj.deletePos(2);
 //obj.printList();


 //obj.insertBeg(40);
 //obj.insertEnd(100);

 //obj.printList();


return 0;
}
