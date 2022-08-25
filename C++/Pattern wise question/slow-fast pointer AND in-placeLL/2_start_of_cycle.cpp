
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
 public:
    int cycleLen(Node * slow){
      Node *curr = slow;

      int count=0;
      bool flag = true;
      while(flag){
        curr = curr->next;
        count++;
        if(curr==slow)
            flag = false;
      }
      return count;
    }

    int findcycle(Node* head){
      Node* slow = head;
      Node* fast = head;
      int len=0;
      while(fast != NULL and fast->next != NULL){
        fast = fast->next->next;
        slow = slow->next;

        if(slow == fast){
            len = cycleLen(slow);
        }
      }

      return startFind(head , len);

    }
    int startFind(Node* head , int len){
       Node* pointer1 = head;
       Node* pointer2 = head;

       while(len > 0){
        pointer2 = pointer2->next;
        len--;
       }

       while(pointer1 != pointer2){
        pointer1 = pointer1->next;
        pointer2 = pointer2->next;
       }

    return pointer1->data;
    }

    void printlist(Node* head){
      Node* curr = head;

      while(curr){
        cout<<curr->data<<" " ;
        curr = curr->next;
      }
      cout<<endl;
     }

};



int main(){
  Node* head = new Node(1);
  head->next = new Node(2);
  head->next->next = new Node(3);
  head->next->next->next = new Node(4);
  head->next->next->next->next = new Node(5);
  head->next->next->next->next->next = new Node(6);

  head->next->next->next->next->next->next = head->next->next;

  Linkedlist obj;
  cout<<"cycle len ::"<<obj.findcycle(head);
  obj.printlist(head);

  }


// Leetcode approach

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *fast=head;
        ListNode *slow=head;

        if(head!=nullptr && head->next!=nullptr)
        {
          while(slow && fast && fast->next!= NULL)
          {
              slow = slow->next;
              fast = fast->next->next;
              if(slow==fast){
                  break;
              }
          }
        if(slow != fast) return NULL;

         slow = head;
         while(slow != fast)
         {

             slow = slow->next;
             fast = fast->next;
         }
          return slow;
        }
        return nullptr;
    }
};


//  my approach

class Solution:
    def hasCycle(self , head):
        slow , fast = head , head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                break
        return fast

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = self.hasCycle(head)
        if(fast ==  None or fast.next == None):
            return None
        slow = head
        while(fast != slow):
            slow = slow.next
            fast = fast.next

        return slow
