#include <iostream>
using namespace std;

struct Node{
 int data;
 Node* next;
};

class List
{
  private:
   Node *head;
  public:
    List()
    {
        head = NULL;
    }
  void deleteBeg()
  {
      if(head==NULL){
        cout<<"Underflow..."<<endl;
      }
      Node *temp;
      temp = head;
      head = head->next;
      free(temp);
  }
  void deleteEnd()
  {
      Node *temp , *pre;
      if(head==NULL){ // list empty
        cout<<"underflow"<<endl;
      }
      else if (head->next== NULL){ // List have  Only one element
          deleteBeg();

      }
     else{
        temp = head;
        while(temp->next != NULL)
        {
            pre = temp;
            temp = temp->next;
        }
        pre->next = NULL;
        free(temp);
     }
  }
};
