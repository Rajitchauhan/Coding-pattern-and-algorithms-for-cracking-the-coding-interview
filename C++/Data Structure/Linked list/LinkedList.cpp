#include <iostream>
using namespace std;

struct Node{
    int data; // 11
    Node *next; // NULL
  };

//Node *head = NULL;

class LinkedList{
   private:
       Node *head;
   public:
       LinkedList()
       {
           head = NULL;
       }
   void insertAtBeg(int val)
   {
       Node *newnode = new Node();
       //(*newnode).data = val;
       newnode->data = val;
       newnode->next = NULL;
       if(head==NULL)
       {
           head = newnode;
       }
       else{

           newnode->next = head;
           head = newnode;
       }
   }
};
