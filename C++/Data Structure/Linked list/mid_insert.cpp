
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
      void insertMid(int val)
      {
          Node *newnode = new Node();
          newnode->data = val;
          newnode->next = NULL;

          if(head==NULL)
          {
              head = newnode;
          }
          else{
             Node *temp , *pre;
             temp = head;
             while(temp->next==)
             {
                 temp = temp->next;
             }
             temp->next = newnode;
          }
      }




};
