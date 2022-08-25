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
     Linkedlist(){ head=NULL; }

     Node* createNode(int data){
       Node* newnode = new Node(data);
       newnode->data =  data;
       newnode->next = NULL;
       return newnode;
     }
     Node* insertNode(Node*head , int data){
       if(head==NULL)
        return createNode(data);

       else head->next = insertNode(head->next , data);


      return head;
     }

    void printList(Node* head){
     if(head ==  NULL) return;
     cout<<head->data<<"->";

     printList(head->next);
    }

    void reversePrint(Node* head){
     if(head == NULL) return;

     reversePrint(head->next);
     cout<<head->data<<"=>";
    }

};


int  main(){
 Linkedlist obj;
 Node* ref_node = NULL;
 ref_node = obj.insertNode(ref_node , 10);
 ref_node = obj.insertNode(ref_node , 20);
 ref_node = obj.insertNode(ref_node , 30);
 ref_node = obj.insertNode(ref_node , 40);
 obj.printList(ref_node);
 cout<<endl;
 cout<<"Reverse list :: "<<endl;
 obj.reversePrint(ref_node);
return 0;
}
