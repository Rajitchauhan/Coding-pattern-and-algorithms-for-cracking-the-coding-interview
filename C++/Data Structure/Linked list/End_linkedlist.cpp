#include <iostream>
using namespace std;

struct Node{
  int data;
  Node *next;
};

class LinkedList{

   Node *head;
   public:
       LinkedList()
       {
           head = NULL;
       }
      void insertEnd(int val)
      {
          Node *newnode = new Node();
          newnode->data = val;
          newnode->next = NULL;

          if(head==NULL)
          {
              head = newnode;
          }
          else{
             Node *temp;
             temp = head;
             while(temp->next==NULL)
             {
                 temp = temp->next;
             }
             temp->next = newnode;
          }
      }




};
