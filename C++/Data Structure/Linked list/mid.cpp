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
    int mid(linkedList)
    {
        Node *slow ,*fast;
        while(fast && fast->next != NULL)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow->data;

    }

};

