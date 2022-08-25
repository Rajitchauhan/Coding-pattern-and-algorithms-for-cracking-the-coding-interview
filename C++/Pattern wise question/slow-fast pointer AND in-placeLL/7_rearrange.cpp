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

      Node* reverseList(Node* head){
        Node* curr=head;
        Node* pre = NULL;
        Node* nxt= NULL;

        while(curr){
            nxt = curr->next;
            curr->next = pre;
            pre = curr;
            curr = nxt;
        }
        return pre;
      }

      Node* getMid(Node* head){
        Node* fast = head;
        Node* slow = head;
        while(fast != NULL and fast->next != NULL){
            slow= slow->next;
            fast = fast->next->next;
        }
        return slow;

      }
     Node* rearrangeList(Node* head){
       if(head == NULL or head->next == NULL)
            return head;

       Node* mid = getMid(head);

       Node* second_half = reverseList(mid);
       Node* first_half = head;

       while(first_half != nullptr and second_half != nullptr){
          Node* temp = first_half->next;
          first_half->next = second_half;
          first_half = temp;

          temp = second_half->next;
          second_half->next  = first_half;
          second_half = temp;

       }

       if(first_half != NULL){
        first_half->next = NULL;
       }

      return head;
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
    Node* newnode = new Node(2);
    newnode->next = new Node(4);
    newnode->next->next = new Node(6);
    newnode->next->next->next = new Node(8);
    newnode->next->next->next->next = new Node(10);
    newnode->next->next->next->next->next = new Node(12);

    Linkedlist obj;

    obj.printList(newnode);
    obj.rearrangeList(newnode);
    obj.printList(newnode);

    return 0;
}

