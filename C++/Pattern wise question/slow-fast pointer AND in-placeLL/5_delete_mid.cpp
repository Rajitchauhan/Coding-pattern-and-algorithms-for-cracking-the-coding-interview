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
      Linkedlist(){ head = NULL; }

      Node* middle_of_list(Node* head){
       Node* fast  = head;
       Node* slow  = head;
       Node* pre = NULL;

       while(fast != NULL and fast->next != NULL){
         pre = slow;
         slow = slow->next;
         fast = fast->next->next;

       }
       pre->next = slow->next;
       delete slow;
       return pre;
      }

    void printList(Node* head){
     Node* curr = head;
     while(curr){
        cout<<curr->data<<" ";
        curr = curr->next;
     }
     cout<<endl;
    }

};

int main()
{
    Node* newnode = new Node(1);
    newnode->next = new Node(2);
    newnode->next->next = new Node(3);
    newnode->next->next->next = new Node(4);
    newnode->next->next->next->next = new Node(5);
    newnode->next->next->next->next->next = new Node(6);

    Linkedlist obj;
    cout<<"middle of list is :: "<<obj.middle_of_list(newnode)->data<<endl;

    obj.printList(newnode);

    return 0;
}


