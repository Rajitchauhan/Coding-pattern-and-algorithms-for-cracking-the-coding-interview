#include <iostream>
using namespace std;

struct Node{
   int data;
   Node* link;
  };
class LinkedList(){
    Node* head;
    public:
        LinkedList(){
            head = NULL;
        }
    void insertAtBeg(int val){
        Node* newnode = new Node();
        newnode->data = val;
        newnode->link=NULL:
        // we create a node
        // now check condition where link is empty or not
        if(head==NULL){
            head=newnode;

        }
         newnode->link=head;
         head = newnode;

    }

    //void print(int )
  };

int main(){
cout<<"linked";

LinkedList obj = new LinkedList;
return 0;
}
